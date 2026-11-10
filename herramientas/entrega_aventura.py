"""Genera la entrega vigente con mapas 2D, SVG y capturas del renderizador."""
from pathlib import Path
import base64
import csv
import html
import xml.etree.ElementTree as ET
from zipfile import ZipFile
from mockups_aventura import mockup
from capturar_aventura import capturar

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ/"documentacion"/"primera_entrega"


def main():
    from preparar_entrega import crear_docx, render
    from documentar_aventura import DOCUMENTOS
    for nombre,contenido in DOCUMENTOS.items():
        (RAIZ/nombre).write_text(contenido.replace("2700","2475"),encoding="utf-8")
    tareas = [
        ("Migrar a aventura 2D","Movimiento, colisiones y ciclo de juego","2026-11-06","TERMINADO","motor.py; aventura.py"),
        ("Crear cuatro mapas","Objetos, personajes, peligros y portales","2026-11-06","TERMINADO","mundos.py"),
        ("Integrar música y efectos","Conservar fondo relajante y prioridad de efectos","2026-11-06","TERMINADO","sonidos.py; aventura.py"),
        ("Probar campaña y renderizado","Rutas, objetivos, daño, herramientas y eventos","2026-11-06","TERMINADO","pruebas/test_logica.py; pruebas/verificar_interfaz.py"),
        ("Revisar documentos 2D","Aceptar GDD storyboard SVG y algoritmos vigentes","2026-11-10","EN REVISION","documentacion/primera_entrega/"),
        ("Mostrar prototipo al docente","Confirmar que la aventura satisface la indicación","2026-11-09","POR HACER","Retroalimentación real del docente"),
        ("Recoger evidencia local","Realizar consultas voluntarias sin datos sensibles","2026-11-09","POR HACER","Registro anónimo de empatía"),
        ("Evaluar con jugadores","Observar movimiento orientación y comprensión","2026-11-10","POR HACER","Registro real de evaluación"),
        ("Equilibrar amenazas","Ajustar centinelas y energía según observaciones","2026-11-11","LISTA GENERAL DE ACTIVIDADES","Comentarios y cambios verificados"),
        ("Actualizar Notion","Registrar la migración y mantener cinco columnas","2026-11-10","POR HACER","Enlace e historial del tablero"),
        ("Capturar evidencia Kanban","Guardar vista general y tarjeta con propiedades","2026-11-11","POR HACER","Capturas fechadas del tablero"),
        ("Ensayar exposición individual","Mostrar análisis diseño y juego en menos de 10 minutos","2026-11-11","POR HACER","Guion y duración del ensayo"),
    ]
    filas = [dict(Nombre=n,Estado=e,Responsable="Jorge Enrique Rentería Mosquera",Fecha=f,Prioridad="Alta",Descripcion=d,Evidencia=v,Fase="Migración a aventura 2D",Observaciones="Registro local; no implica sincronización de Notion. Plazos futuros propuestos.") for n,d,f,e,v in tareas]
    for nombre in ("kanban_notion.csv","kanban_migracion_2d.csv","kanban_primera_entrega.csv"):
        with (DESTINO/nombre).open("w",encoding="utf-8-sig",newline="") as archivo:
            writer = csv.DictWriter(archivo,fieldnames=list(filas[0])); writer.writeheader(); writer.writerows(filas)
    secciones = []
    for titulo,archivo in [("Primera entrega y storyboard","primera_entrega/contenido_adicional.md"),
        ("Análisis del problema","analisis_problema.md"),("GDD de aventura 2D","GDD.md"),
        ("Pensamiento computacional","pensamiento_computacional.md"),("Diseño algorítmico","diseno_algoritmico.md"),
        ("Entrada, proceso y salida","entrada_proceso_salida.md"),("Diccionario de datos","diccionario_datos.md"),
        ("Pruebas y limitaciones","matriz_pruebas.md"),("Manual de usuario","manual_usuario.md"),("Guion de sustentación","presentacion.md")]:
        secciones.append((titulo,(RAIZ/"documentacion"/archivo).read_text(encoding="utf-8")))
    crear_docx(secciones)
    cuerpo = ''.join('<section><h1>'+html.escape(titulo)+'</h1>'+render(texto)+'</section>' for titulo,texto in secciones)
    cuerpo += '<section><h1>Diseños de la aventura 2D</h1><p>SVG vectoriales de menú, exploración y diálogos. Son diseños coherentes con los mapas actuales.</p>'
    for tipo,nombre,nivel in [("menu","mockup_menu.svg",0),("nivel","mockup_nivel.svg",0),("retroalimentacion","mockup_retroalimentacion.svg",0)]:
        (DESTINO/nombre).write_text(mockup(tipo,nivel),encoding="utf-8")
    cuerpo += mockup("menu")
    for nivel in range(4):
        for tipo,prefijo in (("nivel","mockup_mision"),("retroalimentacion","mockup_retroalimentacion_mision")):
            svg = mockup(tipo,nivel)
            (DESTINO/f"{prefijo}_{nivel+1}.svg").write_text(svg,encoding="utf-8")
            if tipo == "retroalimentacion":
                (DESTINO/f"mockup_dialogo_mision_{nivel+1}.svg").write_text(svg,encoding="utf-8")
            cuerpo += '<figure><h2>Distrito '+str(nivel+1)+' · '+('Exploración' if tipo == 'nivel' else 'Diálogo')+'</h2>'+svg+'</figure>'
    cuerpo += '</section>'
    cuerpo += '<section><h1>Tarjetas locales de migración</h1><p>Preparadas para actualizar Notion. La generación de estos CSV no modifica el tablero remoto.</p><table><tr><th>Tarea</th><th>Plazo</th><th>Estado</th><th>Evidencia</th></tr>'
    for fila in filas:
        cuerpo += '<tr>'+''.join('<td>'+html.escape(fila[campo])+'</td>' for campo in ("Nombre","Fecha","Estado","Evidencia"))+'</tr>'
    cuerpo += '</table></section>'
    capturar(DESTINO)
    cuerpo += '<section><h1>Capturas del renderizador</h1><p>Estados iniciales preparados automáticamente en el motor real. No constituyen una evaluación con usuarios.</p>'
    for archivo in ['captura_menu.png']+[f'captura_mision_{i}.png' for i in range(1,5)]:
        datos = base64.b64encode((DESTINO/archivo).read_bytes()).decode()
        cuerpo += f'<figure><h2>{archivo}</h2><img src="data:image/png;base64,{datos}" alt="Captura del renderizador de aventura"/></figure>'
    cuerpo += '</section>'
    css = '''@page{size:A4;margin:15mm}body{font:15px/1.5 'Segoe UI',Arial;background:#f0e3d3;color:#40323d;margin:0}main{max-width:1000px;margin:auto;padding:35px;background:#fff9ef}h1{color:#8b4937;font-size:27px}h2{color:#8b4937;font-size:20px}section{margin-top:30px;padding-top:12px;border-top:2px solid #dbb58d}table{border-collapse:collapse;width:100%;font-size:12px}td,th{border:1px solid #d5bd9e;padding:7px;vertical-align:top}th{background:#ffe5bc}pre{white-space:pre-wrap;padding:14px;background:#f5e6cf;font-size:12px}figure{margin:20px 0;break-inside:avoid}svg,img{width:100%;height:auto;border:1px solid #caa781}button{background:#8b4937;color:white;padding:12px;border:0;cursor:pointer}@media print{body{background:white;font-size:11px}main{padding:0}section{break-before:page}h1,h2{break-after:avoid}tr{break-inside:avoid}button{display:none}}'''
    salida = '<!doctype html><html lang="es"><meta charset="utf-8"><title>CyberQuest · Aventura 2D</title><style>'+css+'</style><main><h1>CyberQuest: Los guardianes del escudo</h1><p>Primera entrega · Aventura 2D · 6 de noviembre de 2026</p><button onclick="window.print()">Imprimir / Guardar PDF</button>'+cuerpo+'</main></html>'
    (DESTINO/'CyberQuest_primera_entrega.html').write_text(salida,encoding="utf-8")
    for archivo in DESTINO.glob('mockup*.svg'):
        ET.parse(archivo)
    with ZipFile(DESTINO/'CyberQuest_primera_entrega.docx') as archivo:
        assert archivo.testzip() is None
        for nombre in archivo.namelist():
            ET.fromstring(archivo.read(nombre))
    print("Entrega 2D generada: documentos, SVG, capturas y HTML autónomo.")


if __name__ == '__main__':
    main()
