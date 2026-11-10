"""Conversores de documentos y entrada del generador de la aventura 2D."""
from pathlib import Path
import sys
import html
import re
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape
RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "documentacion" / "primera_entrega"
sys.path.insert(0,str(RAIZ))
from temas import TEMAS

def bloques(texto):
    lineas = texto.splitlines()
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        if linea.startswith('```'):
            lenguaje = linea[3:]
            i += 1
            codigo = []
            while i < len(lineas) and not lineas[i].startswith('```'):
                codigo.append(lineas[i]); i += 1
            yield ('codigo', '\n'.join(codigo), lenguaje)
        elif linea.startswith('|'):
            filas = []
            while i < len(lineas) and lineas[i].startswith('|'):
                fila = [c.strip() for c in lineas[i].strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c.replace(' ', '')) for c in fila):
                    filas.append(fila)
                i += 1
            yield ('tabla', filas, '')
            continue
        elif linea.startswith('#'):
            yield ('titulo', linea.lstrip('#').strip(), len(linea)-len(linea.lstrip('#')))
        elif linea.strip():
            yield ('parrafo', linea, '')
        i += 1

def formato(texto):
    texto = html.escape(texto)
    texto = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', texto)
    return re.sub(r'`(.+?)`', r'<code>\1</code>', texto)

def render(texto):
    salida = []
    for tipo, valor, extra in bloques(texto):
        if tipo == 'titulo':
            nivel = min(extra+1, 4)
            salida.append(f'<h{nivel}>{formato(valor)}</h{nivel}>')
        elif tipo == 'tabla':
            salida.append('<table>')
            for i, fila in enumerate(valor):
                tag = 'th' if i == 0 else 'td'
                salida.append('<tr>'+''.join(f'<{tag}>{formato(c)}</{tag}>' for c in fila)+'</tr>')
            salida.append('</table>')
        elif tipo == 'codigo':
            if extra != 'mermaid':
                salida.append('<pre>'+html.escape(valor)+'</pre>')
        else:
            salida.append('<p>'+formato(valor)+'</p>')
    return ''.join(salida)

def crear_docx(secciones):
    contenido = []
    def parrafo(texto, estilo='Normal'):
        texto = texto.replace('**', '').replace('`', '')
        return f'<w:p><w:pPr><w:pStyle w:val="{estilo}"/></w:pPr><w:r><w:t xml:space="preserve">{escape(texto)}</w:t></w:r></w:p>'
    contenido.append(parrafo('CyberQuest: Los guardianes del escudo', 'Title'))
    contenido.append(parrafo('Primera entrega · Análisis y diseño · Programación III', 'Subtitle'))
    for titulo, texto in secciones:
        contenido.append(parrafo(titulo, 'Heading1'))
        for tipo, valor, extra in bloques(texto):
            if tipo == 'tabla':
                filas = []
                for fila in valor:
                    filas.append('<w:tr>'+''.join('<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/></w:tcPr>'+parrafo(c)+'</w:tc>' for c in fila)+'</w:tr>')
                contenido.append('<w:tbl><w:tblPr><w:tblBorders>'+''.join(f'<w:{lado} w:val="single" w:sz="4" w:color="D9C4B0"/>' for lado in ['top','left','bottom','right','insideH','insideV'])+'</w:tblBorders></w:tblPr>'+''.join(filas)+'</w:tbl>')
            elif tipo == 'titulo':
                contenido.append(parrafo(valor, 'Heading2'))
            elif tipo == 'codigo':
                if extra != 'mermaid':
                    contenido.extend(parrafo(l, 'Code') for l in valor.splitlines())
            else:
                contenido.append(parrafo(valor))
    contenido.append(parrafo('Mockups visuales', 'Heading1'))
    contenido.append(parrafo('Consultar el menú y las ocho láminas SVG de misión y retroalimentación del mismo paquete. Son mockups, no capturas de ejecución.'))
    for tipo in ('menu', 'nivel', 'retroalimentacion'):
        contenido.append(parrafo('mockup_'+tipo+'.svg'))
    for nivel, tema in enumerate(TEMAS):
        contenido.append(parrafo(f'Misión {nivel+1}: {tema["nombre"]}. Archivos mockup_mision_{nivel+1}.svg y mockup_retroalimentacion_mision_{nivel+1}.svg.'))
    documento = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'+''.join(contenido)+'<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1000" w:right="1000" w:bottom="1000" w:left="1000"/></w:sectPr></w:body></w:document>'
    estilos = '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr></w:rPrDefault></w:docDefaults>'
    for nombre, tam, color in [('Normal',22,'493226'),('Title',40,'A64222'),('Subtitle',26,'805334'),('Heading1',30,'A64222'),('Heading2',25,'805334'),('Code',18,'493226')]:
        estilos += f'<w:style w:type="paragraph" w:styleId="{nombre}"><w:name w:val="{nombre}"/><w:pPr><w:spacing w:after="120"/>' + ('<w:keepNext/>' if nombre.startswith('Heading') else '') + f'</w:pPr><w:rPr><w:color w:val="{color}"/><w:sz w:val="{tam}"/></w:rPr></w:style>'
    estilos += '</w:styles>'
    with ZipFile(DESTINO/'CyberQuest_primera_entrega.docx', 'w', ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>')
        z.writestr('_rels/.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
        z.writestr('word/_rels/document.xml.rels','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
        z.writestr('word/document.xml', documento)
        z.writestr('word/styles.xml', estilos)

if __name__ == '__main__':
    from entrega_aventura import main
    main()
