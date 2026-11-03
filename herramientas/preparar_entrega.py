"""Genera el paquete de análisis y diseño sin dependencias externas."""
from pathlib import Path
import csv
import html
import re
import sys
from zipfile import ZipFile, ZIP_DEFLATED
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "documentacion" / "primera_entrega"
sys.path.insert(0, str(RAIZ))
from mockups_entrega import mockup as mockup_mision
from temas import TEMAS


def mockup(tipo, nivel=0):
    if tipo != "menu":
        return mockup_mision(tipo, nivel)
    partes = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 650" role="img" aria-label="Mockup de '+tipo+'">',
              '<rect width="900" height="650" rx="18" fill="#fff7eb"/>']
    def caja(x, y, w, h, color):
        partes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" rx="5"/>')
    def texto(x, y, t, tam=18, color="#493226"):
        partes.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{tam}" fill="{color}">{html.escape(t)}</text>')
    def boton(y, t, bloqueado=False):
        caja(40, y, 820, 46, "#eee3d4" if bloqueado else "#ffe0b8")
        texto(60, y+29, t, 17, "#796b5b" if bloqueado else "#493226")
    caja(0, 0, 900, 48, "#ffe4c4")
    texto(28, 31, "CYBERQUEST · Defensa Digital", 20)
    texto(735, 30, "Sonido: ON", 15)
    titulo = {"menu": "Elige tu próxima misión", "nivel": "La alerta sospechosa", "retroalimentacion": "¡Una buena decisión protege la ciudad!"}[tipo]
    texto(40, 94, titulo, 27)
    texto(40, 127, "Guardián: Ada    |    XP: "+("100" if tipo == "retroalimentacion" else "0")+"    |    Energía: 3/3    |    Misiones: 0/4", 16)
    if tipo == "menu":
        caja(40, 150, 820, 125, "#ffe7c5")
        caja(65, 169, 30, 30, "#f3ac36")
        for i in range(10):
            x, alto = 180+i*62, 36+(i % 4)*13
            caja(x, 265-alto, 44, alto, ["#e89b69", "#dfb563", "#96b4a1"][i % 3])
            for fila in range(alto//18):
                caja(x+8, 252-fila*18, 7, 6, "#fff2bd")
        sprite = ["..cccc..", ".cccccc.", "..pppp..", "..ptpt..", "..pppp..", ".vvvvvv.", "pvovvovp", "..vvvv..", "..v..v..", ".tt..tt."]
        paleta = {"c":"#b64839", "p":"#ffe1a3", "t":"#493226", "v":"#398578", "o":"#ffbf69"}
        for f, linea in enumerate(sprite):
            for c, pixel in enumerate(linea):
                if pixel in paleta:
                    partes.append(f'<rect x="{85+c*5}" y="{215+f*5}" width="5" height="5" fill="{paleta[pixel]}"/>')
        for i, t in enumerate(["01 · La alerta sospechosa [DISPONIBLE]", "02 · El acceso protegido [BLOQUEADA]", "03 · La red comprometida [BLOQUEADA]", "04 · Operación Escudo Digital [BLOQUEADA]"]):
            boton(300+i*57, t, i > 0)
        boton(540, "Cómo jugar                  Nueva partida")
    else:
        texto(40, 168, "Objetivo: protege a Ada de un mensaje sospechoso.", 18)
        caja(40, 190, 820, 95, "#ffecd6")
        texto(58, 219, "Ada recibe: “Tu cuenta será bloqueada en 10 minutos”.", 20)
        texto(58, 251, "El mensaje pide confirmar su clave desde un enlace.", 18)
        boton(300, "Examinar evidencia")
        texto(40, 378, "Pista: dominio desconocido y petición urgente de información.", 17)
        boton(400, "Abrir la aplicación oficial por mi cuenta para verificar")
        boton(456, "Abrir el enlace del mensaje")
        if tipo == "retroalimentacion":
            caja(40, 517, 820, 65, "#dcead6")
            texto(55, 541, "Defensa reforzada: +100 XP. Energía sin cambios.", 18, "#335538")
            texto(55, 567, "Verificar por un canal independiente evita seguir enlaces engañosos.", 16)
            for i in range(12):
                caja(620+i*16, 145+(i%3)*8, 5, 5, ["#f5a623", "#d35274", "#398578"][i%3])
            boton(594, "Continuar a la siguiente situación")
        else:
            texto(40, 548, "Elige cómo actuar. Cada decisión tiene consecuencias.", 18)
            boton(580, "Continuar [hasta responder: deshabilitado]     Reiniciar misión", True)
    partes.append('</svg>')
    return ''.join(partes)


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
    contenido.append(parrafo('CyberQuest: Defensa Digital', 'Title'))
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


def main():
    adicional = (DESTINO/'contenido_adicional.md').read_text(encoding='utf-8')
    secciones = [('Guía de la primera entrega', adicional)]
    for titulo, archivo in [('1. Análisis del problema','analisis_problema.md'), ('2. GDD inicial','GDD.md'), ('3. Design Thinking','design_thinking.md'), ('4. Pensamiento computacional','pensamiento_computacional.md'), ('5. Diseño algorítmico','diseno_algoritmico.md'), ('6. Entrada, proceso y salida','entrada_proceso_salida.md'), ('7. Diccionario de datos','diccionario_datos.md')]:
        secciones.append((titulo, (RAIZ/'documentacion'/archivo).read_text(encoding='utf-8')))
    # Priorización específica de esta entrega frente al borrador anterior.
    secciones[1] = (secciones[1][0], secciones[1][1] + '\n\nPara esta entrega se prioriza ODS 4, meta 4.4; ODS 9 queda como relación secundaria contextual. Véase la justificación y las fuentes oficiales en la guía inicial.\n')
    contenido = ''.join('<section><h1>'+html.escape(titulo)+'</h1>'+render(texto)+'</section>' for titulo, texto in secciones)
    contenido += '<section><h1>8. Mockups de menú, misiones y retroalimentación</h1><p>Cuatro ambientaciones pixel art: cielo, selva, cielo al atardecer e infierno. Los dibujos y paletas se comparten con el juego. No son capturas de ejecución.</p>'
    for tipo, titulo in [('menu','Menú principal y mapa de misiones'),('nivel','Nivel de juego: investigar y decidir'),('retroalimentacion','Retroalimentación tras una decisión segura')]:
        svg = mockup(tipo)
        (DESTINO/f'mockup_{tipo}.svg').write_text(svg, encoding='utf-8')
        contenido += '<figure><h2>'+titulo+'</h2>'+svg+'<figcaption>Mockup de diseño · CyberQuest · Elaborado con código.</figcaption></figure>'
    for nivel, tema in enumerate(TEMAS):
        for tipo in ('nivel', 'retroalimentacion'):
            svg = mockup(tipo, nivel)
            nombre = f'mockup_mision_{nivel+1}.svg' if tipo == 'nivel' else f'mockup_retroalimentacion_mision_{nivel+1}.svg'
            (DESTINO/nombre).write_text(svg, encoding='utf-8')
            # La primera misión ya está representada por los dos SVG generales.
            if nivel > 0:
                contenido += '<figure><h2>'+html.escape(f'Misión {nivel+1} · {tema["nombre"]} · {tipo}')+'</h2>'+svg+'<figcaption>Mockup de diseño · '+nombre+'</figcaption></figure>'
    contenido += '</section><section><h1>9. Tarjetas Kanban propuestas</h1><p>Preparación para el tablero digital. No acredita un tablero creado ni actividad histórica.</p>'
    with (DESTINO/'kanban_primera_entrega.csv').open(encoding='utf-8', newline='') as f:
        filas = list(csv.reader(f))
    contenido += '<table>'+''.join('<tr>'+''.join('<'+('th' if i == 0 else 'td')+'>'+html.escape(c)+'</'+('th' if i == 0 else 'td')+'>' for c in fila)+'</tr>' for i, fila in enumerate(filas))+'</table></section>'
    css = '''@page{size:A4;margin:16mm}*{box-sizing:border-box}body{font:15px/1.6 'Segoe UI',Arial,sans-serif;background:#f1e9de;color:#493226;margin:0}main{max-width:1000px;margin:auto;background:#fffdf9;padding:45px}header{padding:35px;border-left:8px solid #c36136;background:#fff0db}h1{font-size:26px;color:#983c22;line-height:1.25}h2{font-size:20px;color:#805334;margin-top:28px}h3,h4{color:#805334}section{margin-top:40px;border-top:2px solid #ebd1b2;padding-top:15px}table{width:100%;border-collapse:collapse;font-size:12px;line-height:1.4;margin:16px 0}td,th{padding:8px;border:1px solid #ddc9b1;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:#ffe4c4}tr:nth-child(even){background:#fff6e9}pre{white-space:pre-wrap;background:#fff2df;padding:16px;font-size:12px}figure{margin:22px 0;break-inside:avoid}svg{width:100%;height:auto;border:1px solid #edc59c}figcaption{font-size:12px;color:#805334}a{color:#983c22}.nota{padding:18px;background:#fff0db;border-left:4px solid #c36136}.imprimir{padding:10px 18px;cursor:pointer;background:#a64222;color:white;border:0;font-size:15px}@media print{body{background:white;font-size:11px}main{padding:0;max-width:none}section{break-before:page}h1,h2,h3{break-after:avoid}tr{break-inside:avoid}thead{display:table-header-group}.imprimir{display:none}figure h2{margin-top:0}}'''
    salida = '<!doctype html><html lang="es"><meta charset="utf-8"><title>CyberQuest · Primera entrega</title><style>'+css+'</style><main><header><p>PROGRAMACIÓN III · ANÁLISIS Y DISEÑO</p><h1>CyberQuest: Defensa Digital</h1><p>Primera entrega · 30 de octubre de 2026</p><button class="imprimir" onclick="window.print()">Imprimir / Guardar como PDF</button></header><p class="nota">Paquete para revisión: faltan evidencias reales de investigación, evaluación y tablero Kanban. Completar integrantes y grupo antes de presentar.</p>'+contenido+'</main></html>'
    (DESTINO/'CyberQuest_primera_entrega.html').write_text(salida, encoding='utf-8')
    crear_docx(secciones)
    # Comprobar integridad de Word y cantidad de diseños requeridos.
    import xml.etree.ElementTree as ET
    with ZipFile(DESTINO/'CyberQuest_primera_entrega.docx') as z:
        assert z.testzip() is None
        for nombre in z.namelist():
            ET.fromstring(z.read(nombre))
    for archivo in DESTINO.glob('mockup_*.svg'):
        ET.parse(archivo)
    print('Generados y verificados: HTML, DOCX, menú y SVG de las cuatro misiones y sus respuestas.')


if __name__ == '__main__':
    main()
