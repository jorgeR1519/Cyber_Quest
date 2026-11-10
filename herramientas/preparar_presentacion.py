"""Paquete de los seis productos de primera parte y exposición de 9:30 minutos."""
from pathlib import Path
import base64
import csv
import html
import json
import os
import shutil
import subprocess
import sys
import textwrap
from collections import Counter
from zipfile import ZipFile

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(RAIZ))
DESTINO = RAIZ/"documentacion"/"presentacion_primera_parte"
ANEXOS = DESTINO/"anexos"
FUENTE = RAIZ/"documentacion"/"primera_entrega"
TABLERO = "https://app.notion.com/p/190e3d2ac5714a58a4b651dd81806d15"


def imagen(nombre):
    ruta = DESTINO/nombre
    return 'data:image/png;base64,'+base64.b64encode(ruta.read_bytes()).decode()


def svg_texto(x,y,texto,tam=20,color="#40323d"):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Segoe UI,Arial" font-size="{tam}" fill="{color}">{html.escape(texto)}</text>'


def flujo(nombre, titulo, nodos):
    alto = 140+len(nodos)*112
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {alto}" role="img" aria-label="{html.escape(titulo)}">',
         '<defs><marker id="punta" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#9a6246"/></marker></defs>',
         f'<rect width="1000" height="{alto}" fill="#fff7eb"/>',svg_texto(500,48,titulo,28)]
    for i,(tipo,texto) in enumerate(nodos):
        y = 78+i*112
        if tipo == "decision":
            p.append(f'<path d="M500 {y} L810 {y+43} L500 {y+86} L190 {y+43} Z" fill="#dfe8cf" stroke="#76936e" stroke-width="2"/>')
        else:
            p.append(f'<rect x="190" y="{y}" width="620" height="86" rx="12" fill="{("#f5d4aa" if tipo == "accion" else "#eadce9")}" stroke="#b58764" stroke-width="2"/>')
        lineas = textwrap.wrap(texto,52)
        for j,linea in enumerate(lineas):
            p.append(svg_texto(500,y+38+j*25-(len(lineas)-1)*10,linea,20))
        if i < len(nodos)-1:
            p.append(f'<path d="M500 {y+86} L500 {y+108}" stroke="#9a6246" stroke-width="3" marker-end="url(#punta)"/>')
    p.append('</svg>')
    (DESTINO/nombre).write_text(''.join(p),encoding="utf-8")


def storyboard():
    escenas = [
        ("Elegir la aventura","Nombre y dificultad; comenzar la partida.","captura_menu.png"),
        ("Recibir la misión","Leer instrucciones y hablar con Ada usando E.","captura_dialogo_1.png"),
        ("Explorar el mapa","Mover al guardián y seguir el diario.","captura_mision_1.png"),
        ("Inspeccionar objetos","F revela evidencia; E recoge el paquete.","captura_mision_1.png"),
        ("Ver consecuencias","Entregar, recibir XP y actualizar el progreso.","captura_retroalimentacion.png"),
        ("Proteger las cuentas","Recoger fragmentos, forjar llave y activar defensa.","captura_mision_2.png"),
        ("Contener y reportar","Desconectar estaciones y alcanzar el soporte.","captura_mision_3.png"),
        ("Rescatar y cerrar","Encender balizas, rescatar y activar el núcleo.","captura_mision_4.png")]
    p = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 730" role="img" aria-label="Storyboard de ocho viñetas"><rect width="1200" height="730" fill="#fff7eb"/>',svg_texto(600,40,"Storyboard · Del menú al escudo digital",28)]
    for i,(titulo,texto,archivo) in enumerate(escenas):
        x,y = 15+(i%4)*298,65+(i//4)*320
        p.append(f'<rect x="{x}" y="{y}" width="282" height="300" rx="10" fill="#fff0da" stroke="#c49b77"/>')
        p.append(svg_texto(x+141,y+30,f'{i+1}. {titulo}',18))
        p.append(f'<image x="{x+8}" y="{y+48}" width="266" height="178" href="{imagen(archivo)}"/>')
        for n,linea in enumerate(textwrap.wrap(texto,31)):
            p.append(svg_texto(x+141,y+248+n*21,linea,16))
    p.append('</svg>')
    (DESTINO/'storyboard.svg').write_text(''.join(p),encoding="utf-8")


def preparar_imagenes():
    from capturar_aventura import capturar
    from aventura import Aplicacion
    import pygame as pg
    capturar(DESTINO)
    app = Aplicacion(audio=False)
    try:
        app.nombre = "Guardián"; app.iniciar()
        j = app.juego; j.dialogo = []; j.hechos.add("npc")
        j.carga = "correo"; j.inspeccionados.add("correo")
        o = next(o for o in j.objetos if o["id"] == "oficial")
        j.x,j.y = o["x"]*32+6.,o["y"]*32+4.
        j.interactuar(); app.actualizar(.016); app.dibujar()
        pg.image.save(app.lienzo,str(DESTINO/'captura_retroalimentacion.png'))
    finally:
        app.cerrar()
    for archivo in FUENTE.glob('mockup*.svg'):
        shutil.copy2(archivo,DESTINO/archivo.name)
    # Estado de diseño posterior a una entrega correcta, sin una pregunta de selección.
    fuente = (DESTINO/'mockup_mision_1.svg').read_text(encoding="utf-8")
    fuente = fuente.replace('Guardián · Medio · 0 XP','Guardián · Medio · 100 XP')
    fuente = fuente.replace('Inspecciona y entrega 3 mensajes en su destino seguro.','Mensaje legítimo entregado por el canal oficial. +100 XP. Progreso: 1/3.')
    (DESTINO/'mockup_retroalimentacion.svg').write_text(fuente,encoding="utf-8")


def evidencia_kanban():
    datos = json.loads((ANEXOS/'kanban_notion_2026-11-10.json').read_text(encoding="utf-8"))
    filas = datos['results']
    columnas = ["LISTA GENERAL DE ACTIVIDADES","POR HACER","EN PROCESO","EN REVISION","TERMINADO"]
    conteos = Counter(f['Estado'] for f in filas)
    campos = ["Nombre","Estado","Responsable","date:Fecha:start","Prioridad","Descripcion","Evidencia","Observaciones","url"]
    with (ANEXOS/'kanban_notion_2026-11-10.csv').open('w',encoding='utf-8-sig',newline='') as archivo:
        escritor = csv.DictWriter(archivo,fieldnames=campos,extrasaction='ignore'); escritor.writeheader(); escritor.writerows(filas)
    tablero = '<div class="columnas">'
    for estado in columnas:
        tablero += '<div class="columna"><h2>'+estado+f' ({conteos[estado]})</h2>'
        for f in filas:
            if f['Estado'] != estado: continue
            tablero += '<article><a href="'+html.escape(f['url'])+'">'+html.escape(f['Nombre'])+'</a><p>'+html.escape(f.get('Descripcion',''))+'</p><small>'+html.escape(f.get('Responsable',''))+'<br>Plazo: '+html.escape(f.get('date:Fecha:start','Sin plazo'))+' · '+html.escape(f.get('Prioridad',''))+'</small></article>'
        tablero += '</div>'
    tablero += '</div>'
    ejemplo = next(f for f in filas if f['Nombre'] == 'Estructurar Fácil, Medio y Difícil')
    detalle = '<h2>Detalle de una tarjeta real</h2><table>'+''.join('<tr><th>'+html.escape(campo)+'</th><td>'+html.escape(str(ejemplo.get(campo,'')))+'</td></tr>' for campo in campos)+'</table>'
    encabezado = '<h1>CyberQuest · Evidencia del tablero real</h1><p>Datos consultados el 10 de noviembre de 2026 mediante la conexión autorizada. Esta es una representación de los datos exportados; no es una captura de la interfaz de Notion.</p><p><a href="'+TABLERO+'">Abrir tablero fuente en Notion</a> · '+str(len(filas))+' tarjetas · Trabajo individual.</p>'
    css = '''body{font:14px/1.4 Arial;background:#fff7eb;color:#40323d;padding:25px}.columnas{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.columna{background:#f0e4d3;padding:10px}h2{font-size:15px}article{background:#fffaf1;border:1px solid #d2b897;padding:12px;margin:10px 0;break-inside:avoid}article a{font-weight:bold;color:#86482e}small{font-size:10px}table{border-collapse:collapse;width:100%}td,th{border:1px solid #d2b897;padding:8px;text-align:left;overflow-wrap:anywhere}@page{size:A3 landscape;margin:12mm}@media print{body{padding:0;font-size:11px}article{font-size:10px}article p{font-size:10px}}'''
    (DESTINO/'Evidencia_Kanban.html').write_text('<!doctype html><html lang="es"><meta charset="utf-8"><title>Evidencia Kanban</title><style>'+css+'</style>'+encabezado+tablero+detalle+'</html>',encoding='utf-8')
    return filas,conteos,tablero,detalle


def documentos():
    import preparar_entrega as conversor
    texto = (DESTINO/'informe_primera_parte.md').read_text(encoding='utf-8')
    conversor.DESTINO = DESTINO
    conversor.crear_docx([('Informe de primera parte',texto)])
    (DESTINO/'CyberQuest_primera_entrega.docx').replace(DESTINO/'Informe_primera_parte.docx')
    imagenes = [('Storyboard','storyboard.svg'),('Flujo de navegación','flujo_navegacion.svg'),('Flujo de interacción','flujo_interaccion.svg'),
                ('Menú y selector de dificultad','mockup_menu.svg'),('Nivel jugable','mockup_mision_1.svg'),('Retroalimentación por una entrega','mockup_retroalimentacion.svg')]
    figuras = '<section><h2>Láminas de diseño</h2><p>Mockups vectoriales. El storyboard utiliza imágenes del renderizador como referencia visual.</p>'
    for titulo,archivo in imagenes:
        figuras += '<figure><h3>'+titulo+'</h3>'+(DESTINO/archivo).read_text(encoding='utf-8')+'</figure>'
    figuras += '<figure><h3>Retroalimentación en el prototipo</h3><img src="'+imagen('captura_retroalimentacion.png')+'"/><figcaption>Captura del renderizador en un estado preparado de entrega correcta. No es evaluación con usuarios.</figcaption></figure></section>'
    css = '''@page{size:A4;margin:15mm}body{font:14px/1.55 'Segoe UI',Arial;color:#40323d;background:#eee3d5;margin:0}main{max-width:1000px;margin:auto;background:#fffdf8;padding:35px}header{padding:30px;background:#ffedd3;border-left:8px solid #a76342}h1{color:#87452e;font-size:32px}h2{font-size:24px;color:#87452e;break-before:page;margin-top:30px}h3{font-size:19px;color:#795342}table{width:100%;border-collapse:collapse;font-size:11px;line-height:1.4;margin:14px 0}th,td{border:1px solid #d3bda0;padding:7px;vertical-align:top;overflow-wrap:anywhere}th{background:#ffe9cc}pre{white-space:pre-wrap;background:#f5e8d5;padding:15px;font:11px/1.5 Consolas,monospace}figure{margin:20px 0;break-inside:avoid}svg,img{width:100%;height:auto}figcaption{font-size:11px;color:#795342}a{color:#87452e}button{padding:12px;background:#87452e;color:white;border:0;cursor:pointer}@media print{body{font-size:11px;background:white}main{padding:0}h2,h3{break-after:avoid}tr{break-inside:avoid}figure h3{margin-top:0}button{display:none}}'''
    html_doc = '<!doctype html><html lang="es"><meta charset="utf-8"><title>Informe primera parte</title><style>'+css+'</style><main><header><h1>CyberQuest</h1><p>Los guardianes del escudo · Primera parte: análisis y diseño</p><p>Jorge Enrique Rentería Mosquera · Programación III · Corte: 10/11/2026</p><button onclick="window.print()">Imprimir / Guardar PDF</button></header>'+conversor.render(texto.split('\n',1)[1])+figuras+'</main></html>'
    (DESTINO/'Informe_primera_parte.html').write_text(html_doc,encoding='utf-8')
    instrumentos = (DESTINO/'instrumentos_investigacion.md').read_text(encoding='utf-8')
    (DESTINO/'Instrumentos_investigacion.html').write_text('<!doctype html><html lang="es"><meta charset="utf-8"><title>Instrumentos por aplicar</title><style>'+css+'</style><main>'+conversor.render(instrumentos)+'</main></html>',encoding='utf-8')


def presentacion(conteos):
    diapositivas = []
    def agregar(titulo,cuerpo,sub=''):
        diapositivas.append((titulo,sub,cuerpo))
    def lista(items):
        return '<ul>'+''.join('<li>'+html.escape(x)+'</li>' for x in items)+'</ul>'
    def foto(archivo):
        return '<img src="'+imagen(archivo)+'"/>'
    agregar('CyberQuest','<div class="dos"><div><h2>Los guardianes del escudo</h2><p>Aventura educativa 2D de exploración y protección digital.</p><p><strong>Jorge Enrique Rentería Mosquera</strong><br>Programación III · Ingeniería de Sistemas<br>Institución Universitaria Antonio José Camacho</p><p class="etiqueta">Primera parte · Análisis y diseño</p></div>'+foto('captura_menu.png')+'</div>','Corte: 10 de noviembre de 2026 · Exposición individual')
    agregar('1. Problema, público y ODS','<div class="dos"><div>'+lista(['Hipótesis: dificultades para reconocer engaños, proteger cuentas y responder ante alertas.','Público propuesto: estudiantes y jóvenes usuarios de servicios digitales.','El problema local todavía requiere consultas reales.'])+'</div><div class="tarjeta"><h2>ODS 4 · Educación de calidad</h2><p>Práctica propuesta de competencias digitales: verificar, proteger y reportar.</p><p>Relación con meta 4.4. No se afirma impacto medido.</p><p class="pequeno">Fuente: sdgs.un.org/goals/goal4</p></div></div>')
    agregar('2. Propuesta de valor','<div class="dos"><div>'+lista(['El guardián recorre mundos, conversa y manipula objetos.','Cada misión conecta una acción del juego con una práctica de seguridad.','Hay consecuencias, recursos, progresión y cierre narrativo.'])+'</div>'+foto('captura_mision_1.png')+'</div>','La aventura 2D responde a la indicación docente comunicada por el autor.')
    agregar('3. Design Thinking','<div class="dos"><div>'+lista(['Empatizar: hipótesis y comentarios reales del autor; consultas externas pendientes.','Definir: público, pregunta de diseño y objetivos.','Idear: elección de aventura 2D por alcance y encargo.','Prototipar: mapas, personajes, objetos y reglas.','Evaluar: pruebas técnicas y ajustes; jugadores externos pendientes.'])+'</div><div class="tarjeta"><h2>Comentarios que cambiaron el diseño</h2><p>“No entiendo qué hacer” → tutorial y siguiente paso.</p><p>“Solo se mueven de izquierda a derecha” → persecución y cobertura.</p><p>Petición de tres modos → Fácil, Medio y Difícil.</p></div></div>')
    agregar('4. Historia, personajes y niveles','<p>Sombra apaga las defensas de la ciudad. El guardián recibe ayuda de Ada, Leo e Iris y rescata a Noa, Sol y Teo.</p><table><tr><th>Mundo</th><th>Misión</th><th>Aprendizaje propuesto</th></tr><tr><td>Cielo</td><td>Inspeccionar y entregar mensajes</td><td>Verificación y cuarentena</td></tr><tr><td>Selva</td><td>Forjar llave y activar segunda defensa</td><td>Clave única y segundo factor</td></tr><tr><td>Atardecer</td><td>Desconectar estaciones y reportar</td><td>Contención y comunicación</td></tr><tr><td>Lava</td><td>Balizas, rescates y núcleo</td><td>Integrar las defensas</td></tr></table>')
    agregar('5. Reglas y dificultad','<div class="dos"><div><table><tr><th>Modo</th><th>Energía</th><th>Radio</th><th>Recuperación</th></tr><tr><td>Fácil</td><td>7</td><td>5</td><td>Hasta 2</td></tr><tr><td>Medio</td><td>5</td><td>3</td><td>Hasta 1</td></tr><tr><td>Difícil</td><td>3</td><td>1</td><td>0</td></tr></table><p>Los enemigos detectan, avisan, persiguen y pierden el rastro. Las paredes sirven de cobertura y el refugio está protegido.</p></div><div class="tarjeta"><h2>Acciones y consecuencias</h2>'+lista(['Mover: WASD o flechas.','Interactuar: E. Inspeccionar: F.','Impulso: Espacio. Guía: T.','Daño: −1 energía y hasta −20 XP.','Portal: objetivos completos y +200 XP.','Victoria: activar el núcleo tras cuatro distritos.'])+'</div></div>')
    agregar('6. Storyboard',(DESTINO/'storyboard.svg').read_text(encoding='utf-8'),'Del menú a la exploración, las consecuencias y el cierre de la historia.')
    agregar('7. Mockups y experiencia','<div class="tres"><div><h2>Menú</h2>'+foto('captura_menu.png')+'</div><div><h2>Exploración</h2>'+foto('captura_mision_1.png')+'</div><div><h2>Retroalimentación</h2>'+foto('captura_retroalimentacion.png')+'</div></div><p>Diario persistente, destino resaltado, guía gratuita y textos que pausan el mundo. Imágenes del prototipo en estados preparados.</p>','Demostración breve: hablar con Ada, inspeccionar un paquete y recogerlo.')
    agregar('8. Pensamiento computacional y algoritmo','<div class="dos"><div><pre>Leer entradas\n→ Validar movimiento y colisiones\n→ Actualizar amenazas\n→ Interactuar con objetos\n→ Comprobar requisitos\n→ Conceder premio una sola vez\n→ Habilitar portal o explicar faltantes</pre></div><div>'+lista(['Descomposición: mundo, reglas, interfaz, inteligencia y audio.','Patrones: objetos con id, tipo, posición y requisitos.','Abstracción: representar prácticas digitales con acciones del mundo.','Listas, diccionarios, conjuntos, ciclos y métodos resuelven necesidades concretas.'])+'</div></div>')
    resumen = ''.join('<div class="contador"><strong>'+str(conteos.get(e,0))+'</strong><span>'+e+'</span></div>' for e in ['LISTA GENERAL DE ACTIVIDADES','POR HACER','EN PROCESO','EN REVISION','TERMINADO'])
    agregar('9. Kanban, validación y próximos pasos','<div class="contadores">'+resumen+'</div><div class="dos"><div><h2>Avance verificable</h2>'+lista(['Tablero real con tareas, responsable, plazos y evidencias.','19 pruebas unitarias y comprobación gráfica.','Documentos y mockups de la aventura actual.'])+'</div><div><h2>Próximos pasos</h2>'+lista(['Aplicar consultas voluntarias.','Evaluar claridad y dificultad con jugadores.','Registrar resultados y ensayar la sustentación.'])+'</div></div><p class="pequeno">'+TABLERO+'</p>','Validación técnica realizada; evaluación con participantes pendiente.')
    css = '''*{box-sizing:border-box}body{margin:0;background:#292534;font:22px/1.45 'Segoe UI',Arial;color:#40323d}.slide{display:none;width:1200px;height:675px;padding:38px 50px;background:#fff6e8;position:relative;flex-direction:column;overflow:hidden}.slide.active{display:flex}h1{font-size:39px;line-height:1.13;color:#8b4937;margin:8px 0 18px}h2{font-size:24px;color:#8b4937;margin:10px 0}p{margin:10px 0}.sub{font-size:16px;color:#80614f;margin-bottom:16px}.dos{display:grid;grid-template-columns:1fr 1fr;gap:35px;align-items:start}.dos>img{width:100%;margin-top:20px}.tres{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.tres img{width:100%;border:1px solid #bda589}ul{padding-left:24px;margin:6px 0}li{margin:10px 0}table{border-collapse:collapse;width:100%;font-size:21px}th,td{padding:12px;border-bottom:2px solid #dfc6a8;text-align:left}th{background:#ffdeb1}.tarjeta{background:#f2e1ca;border:1px solid #dbc09e;padding:22px;border-radius:14px}.pequeno{font-size:15px;overflow-wrap:anywhere}.etiqueta{background:#dbe7cf;padding:10px;font-size:19px}pre{white-space:pre-wrap;background:#f2e1ca;border-left:7px solid #b7764a;padding:20px;font:21px/1.7 Consolas,monospace;margin:0}svg{max-height:475px;width:100%;height:auto}.pie{position:absolute;bottom:18px;left:50px;right:50px;font-size:14px;color:#80614f;display:flex;justify-content:space-between}.contadores{display:flex;gap:12px;margin:10px 0 25px}.contador{flex:1;background:#f0dfc5;padding:12px;text-align:center;border-radius:12px}.contador strong{display:block;font-size:36px;color:#8b4937}.contador span{font-size:12px;display:block}.controles{position:fixed;bottom:12px;right:15px;z-index:2;background:#ffffffeb;padding:7px;font-size:14px}button{cursor:pointer;padding:8px;border:0;background:#dec49e;color:#40323d}.escenario{display:flex;min-height:100vh;align-items:center;justify-content:center}@page{size:320mm 180mm;margin:0}@media print{body{background:white}.escenario{display:block;min-height:0}.slide{display:flex!important;width:320mm;height:180mm;break-after:page;padding:10mm 13mm}.slide:last-child{break-after:auto}.controles{display:none}}'''
    cuerpo = ''
    for i,(titulo,sub,contenido) in enumerate(diapositivas):
        cuerpo += '<section class="slide'+(' active' if i == 0 else '')+'"><h1>'+titulo+'</h1><div class="sub">'+sub+'</div>'+contenido+'<div class="pie"><span>CyberQuest · Primera parte · Jorge Enrique Rentería Mosquera</span><span>'+str(i+1)+' / 10</span></div></section>'
    script = '''let indice=Math.max(0,Math.min(9,(parseInt(location.hash.slice(1))||1)-1));const slides=[...document.querySelectorAll('.slide')];function mostrar(n){indice=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,i)=>s.classList.toggle('active',i===indice));location.hash=indice+1;}document.addEventListener('keydown',e=>{if(['ArrowRight',' ','PageDown'].includes(e.key)){e.preventDefault();mostrar(indice+1)}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();mostrar(indice-1)}});mostrar(indice);'''
    salida = '<!doctype html><html lang="es"><meta charset="utf-8"><title>CyberQuest · Presentación de 10 minutos</title><style>'+css+'</style><div class="escenario">'+cuerpo+'</div><div class="controles"><button onclick="mostrar(indice-1)">Anterior</button> Flechas ← → <button onclick="mostrar(indice+1)">Siguiente</button> <button onclick="window.print()">Imprimir</button></div><script>'+script+'</script></html>'
    (DESTINO/'Presentacion_10_minutos.html').write_text(salida,encoding='utf-8')
    return diapositivas


def guion():
    tiempos = ['0:00–0:35','0:35–1:25','1:25–2:10','2:10–3:15','3:15–4:15','4:15–5:20','5:20–6:05','6:05–7:25','7:25–8:30','8:30–9:30']
    textos = [
        'Presento CyberQuest, una aventura educativa 2D. Esta entrega se centra en el análisis y diseño; el prototipo permite comprobar que la propuesta es viable.',
        'Parto de una hipótesis sobre dificultades de protección digital en estudiantes. Aún no tengo encuestas externas contestadas. La relación principal es ODS 4 por la práctica de competencias digitales; no afirmo impacto medido.',
        'La propuesta transforma prácticas de seguridad en acciones del mundo: inspeccionar, transportar, activar y reportar. Elegí una aventura 2D para responder al juego tradicional solicitado y mantener un alcance viable.',
        'Explico las cinco fases y distingo lo preparado de lo validado. Mis comentarios reales sobre orientación y dificultad produjeron cambios; las consultas externas siguen pendientes. Muestro los instrumentos sin respuestas.',
        'Cuento brevemente la amenaza de Sombra y el papel del guardián, Ada, Leo e Iris. Recorro los cuatro distritos y conecto cada misión con su aprendizaje.',
        'Explico energía, puntos, portales, victoria y derrota. Muestro la diferencia entre Fácil, Medio y Difícil y cómo el refugio, la cobertura y el impulso ayudan a escapar.',
        'Uso el storyboard para recorrer el viaje del jugador desde el menú hasta el núcleo, sin leer todas las celdas.',
        'Muestro menú, nivel y retroalimentación. Si la demostración está preparada, abro el juego en Fácil: avanzo textos, hablo con Ada, me acerco al paquete y pulso F y E. Limito la demostración a 45 segundos; si surge un problema, uso las capturas del prototipo.',
        'Explico el algoritmo de interacción: encontrar objeto, validar requisitos, modificar estado y conceder una recompensa una sola vez. Relaciono listas, ciclos, condiciones y métodos con necesidades del juego.',
        'Abro el tablero real y una tarjeta con responsable, plazo y evidencia. Explico las pruebas técnicas y sus límites. Cierro con lo pendiente: consultas, evaluación y ajustes. Declaro la asistencia de IA.']
    texto = '# Guion de sustentación · 9 minutos y 30 segundos\n\nAutor: Jorge Enrique Rentería Mosquera. Reservar 30 segundos de margen. No leer las diapositivas palabra por palabra.\n\n'
    for i,(tiempo,contenido) in enumerate(zip(tiempos,textos),1):
        texto += f'## Diapositiva {i} · {tiempo}\n\n{contenido}\n\n'
    texto += '''# Preparación de la demostración

1. Ejecutar `py main.py` antes de exponer, elegir Fácil y comprobar sonido o silenciar con M durante la aventura.
2. Tener abiertos el menú, el PDF y el tablero de Notion. La presentación HTML se avanza con flechas.
3. En el juego, E/Enter cierra cada diálogo. Hablar con Ada. El siguiente paquete está hacia la derecha y ligeramente abajo del refugio.
4. F inspecciona y abre un texto; cerrarlo con E. E recoge el paquete. Para la entrega completa, seguir la ruta y terminal indicada por el diario.
5. La demostración no debe consumir todo el tiempo: usar la captura de entrega para mostrar la consecuencia si hace falta.

# Preguntas probables

¿Ya probaste que enseña? La intención educativa está diseñada; las pruebas ejecutadas verifican reglas y renderizado. Para afirmar aprendizaje necesito evaluar personas.

¿Por qué es un juego tradicional? Porque controlo un personaje dentro de mapas con colisiones, amenazas, objetos, objetivos espaciales, historia y finales.

¿Qué hizo la IA? Asistió en código y borradores; yo debo comprender, revisar y defender el resultado.

¿Qué falta de esta parte? Recoger evidencia local externa, aplicar evaluación y completar los datos de grupo si corresponden. Los instrumentos están listos y esas tareas siguen pendientes en Kanban.
'''
    (DESTINO/'guion_10_minutos.md').write_text(texto,encoding='utf-8')


def main():
    DESTINO.mkdir(exist_ok=True); ANEXOS.mkdir(exist_ok=True)
    preparar_imagenes(); storyboard()
    flujo('flujo_navegacion.svg','Flujo de navegación y avance',[
        ('inicio','Menú: nombre y dificultad'),('accion','Introducción, guía y conversación del refugio'),
        ('accion','Explorar: moverse, inspeccionar y recoger objetos'),('accion','Activar mecanismos y entregar con consecuencias'),
        ('decision','¿Objetivos completos? No: seguir explorando'),('accion','Sí: usar portal y avanzar al siguiente distrito'),
        ('decision','¿Cuarto distrito completo? No: nueva misión'),('inicio','Sí: activar núcleo y mostrar victoria')])
    flujo('flujo_interaccion.svg','Interacción con objetos y requisitos',[
        ('inicio','Pulsar E / Enter'),('decision','¿Hay diálogo? Sí: avanzar texto y terminar'),
        ('accion','Si no: buscar objeto cercano, sin pared intermedia'),('decision','¿Existe objeto? No: pedir que se acerque'),
        ('accion','Sí: comprobar conversación, inventario y requisitos'),('decision','¿Cumple? No: explicar lo que falta'),
        ('accion','Sí: actualizar estado y premiar una sola vez'),('inicio','Mostrar consecuencia, siguiente paso y progreso')])
    filas,conteos,_,_ = evidencia_kanban()
    documentos(); presentacion(conteos); guion()
    entorno = os.environ.copy(); entorno['PYTHONIOENCODING'] = 'utf-8'
    if '--solo-documentos' not in sys.argv:
        prueba = subprocess.run([sys.executable,'-m','unittest','discover','-s','pruebas','-v'],cwd=RAIZ,capture_output=True,text=True,encoding='utf-8',errors='replace',env=entorno)
        grafica = subprocess.run([sys.executable,'pruebas/verificar_interfaz.py'],cwd=RAIZ,capture_output=True,text=True,encoding='utf-8',errors='replace',env=entorno)
        (ANEXOS/'verificacion_2026-11-10.txt').write_text('Verificación del 10 de noviembre de 2026\n\n'+prueba.stdout+prueba.stderr+'\nComprobación gráfica:\n'+grafica.stdout+grafica.stderr,encoding='utf-8')
        if prueba.returncode or grafica.returncode:
            raise RuntimeError('Revisar el informe de verificación antes de presentar.')
    with ZipFile(DESTINO/'Informe_primera_parte.docx') as archivo:
        assert archivo.testzip() is None
    for archivo in DESTINO.glob('*.svg'):
        import xml.etree.ElementTree as ET
        ET.parse(archivo)
    resumen = '# Abrir primero\n\n1. Presentacion_10_minutos.pdf o su HTML (flechas para avanzar).\n2. Informe_primera_parte.pdf para entregar; DOCX para editar.\n3. guion_10_minutos.md para ensayar 9:30 minutos.\n4. Evidencia_Kanban.pdf y el tablero real enlazado.\n5. Instrumentos_investigacion.pdf: encuesta y observación por aplicar, sin respuestas inventadas.\n\nCompletar grupo si corresponde. La presentación se prepara para el 11 de noviembre indicado por el autor; la imagen docente indica el 12. Consultas y evaluación externas pendientes. El JSON y CSV de anexos son exportaciones reales de Notion; la vista imprimible no se presenta como captura del servicio.\n'
    (DESTINO/'ABRIR_PRIMERO.md').write_text(resumen,encoding='utf-8')
    print(f'Paquete generado: 10 diapositivas, seis productos, {len(filas)} tarjetas verificadas, 19 pruebas y comprobación gráfica aprobadas.')


if __name__ == '__main__':
    main()
