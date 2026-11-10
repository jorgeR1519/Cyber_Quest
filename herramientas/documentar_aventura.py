"""Documentación vigente de la aventura 2D, sin resultados de campo ficticios."""
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[1]

DOCUMENTOS = {
"documentacion/design_thinking.md": '''# Design Thinking · Migración a aventura 2D

| Fase | Actividad y estado real | Evidencia |
|---|---|---|
| Empatizar | Consultas a estudiantes sobre hábitos y dificultades: pendientes | Plantilla de participantes en la primera entrega |
| Definir | Hipótesis de dificultad para reconocer engaños y proteger cuentas; pendiente de contrastar localmente | Análisis del problema |
| Idear | Se comparó la propuesta inicial de decisiones con la aventura 2D; se adoptó la aventura tras la indicación docente comunicada por el autor | Historial del prototipo anterior y GDD actual |
| Prototipar | Motor de movimiento, cuatro mapas, personajes, objetos y misiones implementados | Código, SVG y capturas del renderizador |
| Evaluar | Pruebas automatizadas ejecutadas; balance y evaluación con personas pendientes | Matriz de pruebas y registros reales futuros |

Preguntas propuestas para empatizar: ¿qué señales te hacen desconfiar de un mensaje?, ¿cómo proteges distintas cuentas?, ¿qué harías ante una alerta desconocida? No pedir contraseñas ni datos privados. Registrar participante anónimo, fecha, respuesta, interpretación y cambio de diseño. No inventar respuestas ni atribuir resultados de automatización a usuarios.

En la evaluación jugable, observar si el participante descubre cómo hablar con Ada, inspeccionar, transportar y entregar. Registrar dónde se pierde, cuánto entiende de los iconos y si distingue peligro, pared y objeto. Probar también el impulso y la visibilidad del diario. Ajustar dificultad después de estas observaciones.
''',
"README.md": '''# CyberQuest: Los guardianes del escudo

Aventura 2D vista desde arriba para Programación III. Controla al guardián, explora cuatro mapas, habla con personajes, recoge objetos, esquiva centinelas y recupera las defensas de la ciudad. Las misiones se completan actuando en el mundo; no hay preguntas de selección.

## Instalar y jugar

Requiere Python 3.10 o posterior. En Windows, desde esta carpeta:

```powershell
py -m pip install -r requirements.txt
py main.py
```

Si tu instalación usa `python`, reemplaza `py` por `python`. Se utiliza pygame-ce 2.5.8. No necesitas descargar imágenes: el pixel art se dibuja con código. El audio original de fondo y efectos utiliza winsound en Windows; el juego puede ejecutarse sin sonido en otros sistemas.

## Controles

| Tecla | Acción |
|---|---|
| WASD o flechas | Mover al personaje |
| E o Enter | Hablar, recoger, activar, entregar y continuar diálogos |
| F | Inspeccionar el objeto cercano o el mensaje transportado |
| H | Llamar a Ada por radio; tres usos por partida |
| Espacio + dirección | Impulso para esquivar; recarga de 1,2 segundos |
| Esc | Pausar o continuar |
| R | Solicitar reinicio del distrito; confirmar con Enter |
| M | Silenciar o activar música y efectos durante la aventura |

## Historia y misiones

Sombra está apagando los cuatro distritos. Con Ada, Leo e Iris debes recuperar las defensas y rescatar a los habitantes.

1. Cielo: inspecciona tres paquetes y entrega los legítimos al correo oficial y los fraudes a cuarentena.
2. Selva: reúne tres fragmentos, forja una llave única y activa el segundo factor con un sello de recuperación.
3. Atardecer: desconecta tres estaciones comprometidas y entrega el reporte al soporte.
4. Lava: reúne cristales, activa tres balizas, rescata a tres habitantes y enciende el núcleo.

Cada distrito comienza con una introducción. Habla con el personaje del refugio para activar la misión. El portal solo abre cuando cumples los objetivos.

## Recursos y reglas

Energía inicial y máxima: 5. Un contacto con amenaza o una entrega insegura resta una energía y hasta 20 XP; vuelves al refugio conservando objetos. Hay 1,5 segundos de protección tras recibir daño. El impulso protege brevemente y nunca atraviesa paredes.

Recoger fragmentos, sellos y cristales concede 25 XP. Entregas correctas, mecanismos, estaciones, reportes, balizas y rescates conceden 100 XP. Completar un distrito concede 200 XP y recupera una energía hasta 5. Las frutas recuperan una energía y no se consumen si ya está completa. No se repiten recompensas de objetos usados. El máximo de una partida sin daño es 2700 XP.

Reiniciar restaura puntos, energía, llamadas y objetivos al inicio del distrito actual. Energía cero: derrota con opción de reintentar distrito o empezar de nuevo. Activar el núcleo tras completar los cuatro mapas: victoria. No hay guardado en disco: cerrar pierde la partida.

## Código

- `main.py`: inicia la aventura.
- `aventura.py`: dibujo Pygame, teclado, interfaz y ciclo de juego a 60 FPS.
- `motor.py`: movimiento, colisiones, recursos, herramientas y condiciones de objetivos.
- `mundos.py`: mapas y objetos de los cuatro distritos.
- `temas.py`: paletas y decoraciones pixel art.
- `sonidos.py`: música y efectos originales; el fondo se interrumpe durante los efectos y vuelve después.
- `interfaz.py`, `logica_juego.py`, `misiones.py`: importaciones de compatibilidad hacia la aventura actual.
- `historial/prototipo_cuestionario/`: copia de la versión anterior, conservada como historial; no es la aplicación activa.

## Verificación

```powershell
py -m unittest discover -s pruebas -v
py pruebas/verificar_interfaz.py
```

Se comprobaron las rutas transitables de todos los objetos y la finalización de las cuatro misiones mediante movimiento e interacción. La prueba de rutas desactiva los centinelas para ser determinista: no mide el balance de dificultad de una partida humana. La comprobación gráfica utiliza el controlador de vídeo dummy y verifica eventos y renderizado sin abrir una ventana. Falta evaluar claridad y dificultad con personas reales.

## Entrega

La carpeta `documentacion/primera_entrega/` contiene el GDD, storyboard, SVG, capturas del renderizador y documentos generados de la versión 2D. Las entrevistas y la evaluación con usuarios siguen pendientes. El tablero Notion existente debe actualizarse con las tareas de migración; no se afirma haberlo modificado automáticamente.

Se utilizó asistencia de IA (Codex) para programación, pruebas y borradores. El autor debe comprender el código y declarar el uso según las orientaciones del curso. Los escenarios son ficticios; no se introducen contraseñas reales.
''',
"documentacion/GDD.md": '''# GDD · CyberQuest: Los guardianes del escudo

Versión 2D de aventura · 6 de noviembre de 2026. Autor: Jorge Enrique Rentería Mosquera. Trabajo individual, Programación III.

## Concepto y propósito

Aventura 2D vista desde arriba, con exploración por teclado, objetos, personajes y obstáculos. El jugador protege una ciudad digital completando objetivos dentro de cuatro mapas. El aprendizaje surge de inspeccionar, transportar, activar, contener y rescatar; no se presenta un cuestionario.

Público: estudiantes y jóvenes que usan servicios digitales. Problema inicial: posibles dificultades para reconocer engaños y proteger cuentas; la presencia local de este problema sigue pendiente de validación mediante consultas reales. Relación principal con ODS 4, meta 4.4, como propuesta de práctica de competencias digitales, sin atribuir impacto medido.

## Historia

Sombra ha apagado las defensas que conectan los cuatro distritos. El guardián parte del refugio de Ada, cruza la selva de Leo, auxilia a Iris al atardecer y entra en la fortaleza de lava. Al reunir las defensas y rescatar a los habitantes puede reactivar el escudo de la ciudad.

## Personajes

| Personaje | Rol jugable |
|---|---|
| Guardián | Personaje controlable por el jugador |
| Ada | Guía inicial y apoyo por radio |
| Leo | Custodio de las llaves de la selva |
| Iris | Técnica del distrito de estaciones |
| Noa, Sol y Teo | Habitantes que deben ser rescatados en la fortaleza |
| Sombra y centinelas | Amenazas móviles que se evitan con movimiento e impulso |

## Niveles y relación educativa

| Nivel | Mundo y objetivo | Mecánica | Aprendizaje propuesto |
|---|---|---|---|
| 1. El correo de las nubes | Cielo: entregar tres mensajes | Inspeccionar evidencia, transportar uno por vez, elegir físicamente la terminal | Verificar dominios y aislar mensajes fraudulentos |
| 2. Las llaves de la selva | Selva: renovar dos defensas | Recoger tres fragmentos, usar forja, buscar sello, activar segundo factor | Clave única y protección adicional se complementan |
| 3. Estaciones al atardecer | Cielo al atardecer: detener propagación | Desconectar tres estaciones y alcanzar el soporte | Contener y reportar un incidente |
| 4. El corazón de Sombra | Fortaleza de lava: rescatar y activar núcleo | Gestionar tres cristales, encender balizas, rescatar habitantes, esquivar centinelas | Integrar protección, coordinación y respuesta |

## Controles y experiencia

WASD o flechas para moverse; E/Enter para interactuar; F para inspeccionar; H para radio; Espacio para impulso; Esc para pausa; R para solicitar reinicio; M para audio durante la aventura. Los diálogos se avanzan con E/Enter y detienen las amenazas mientras se leen. No hay límite de tiempo. La ventana puede redimensionarse manteniendo la proporción del área lógica 1200 × 800.

Los mapas tienen 26 × 17 casillas de 32 píxeles. Paredes de nubes, árboles o piedra impiden el paso. Los peligros se reconocen por casillas brillantes y los centinelas por su forma y movimiento. Los objetos tienen iconos, el escáner muestra su función y el nombre aparece al acercarse. El diario lateral conserva objetivo, progreso, mochila y controles.

## Reglas y recursos

Energía inicial/máxima 5. Daño: −1 energía y −20 XP con mínimo 0; retorno al refugio sin perder objetos; protección de 1,5 segundos. El impulso dura 0,16 segundos, recarga en 1,2 segundos y protege brevemente sin atravesar paredes. Hay una fruta reparadora por nivel, recupera 1 y no se consume con energía completa.

Fragmentos, sello y cristales: +25 XP. Objetivos de entrega, forja, segundo factor, estaciones, reporte, balizas y rescates: +100 XP. Completar distrito: +200 XP y +1 energía hasta el máximo. Máximo sin daño: 2700 XP. La recompensa de cada objeto solo se obtiene una vez. El escáner es gratuito y la radio dispone de tres llamadas por partida.

El primer distrito exige haber inspeccionado el mensaje antes de entregarlo. Una terminal incorrecta causa daño y conserva el paquete para corregir la acción. La forja requiere tres fragmentos; el segundo factor requiere la forja y el sello. El reporte requiere tres estaciones desconectadas. Cada rescate requiere su baliza activa; cada baliza consume un cristal. El portal final exige las tres balizas y tres rescates.

## Avance y finales

Se habla con el personaje del refugio antes de activar objetivos. Los portales se abren solo al terminar la misión. Victoria: activar el núcleo al completar los cuatro distritos. Derrota: energía cero. Reiniciar restaura el estado de entrada al distrito, incluidas las llamadas y los puntos, conservando el avance de distritos anteriores. Empezar otra aventura reinicia todo. No hay guardado persistente.

## Estética, sonido y narrativa

Pixel art dibujado con formas propias: personaje animado, tiles, objetos flotantes y centinelas con alas. Cada distrito utiliza una paleta completa. La música original relajante se reproduce en bucle; los efectos la interrumpen y el fondo vuelve al terminar. Se puede silenciar. La información importante también se comunica por texto.

## Navegación

Menú y nombre → introducción → exploración → interacción y diálogos → objetivo completo → portal → siguiente distrito → victoria. Daño puede llevar a derrota; pausa permite reiniciar con confirmación. El storyboard y los SVG actuales se encuentran en la carpeta de primera entrega.
''',
"documentacion/manual_usuario.md": '''# Manual de usuario · Aventura 2D

Instala las dependencias con `py -m pip install -r requirements.txt` y ejecuta `py main.py`. Escribe un nombre y pulsa Enter o Comenzar aventura.

Muévete con WASD o flechas. E/Enter habla con personajes, recoge objetos, activa mecanismos y continúa textos. F inspecciona un objeto cercano o el mensaje transportado. H solicita una de las tres ayudas por radio. Espacio mientras te mueves activa el impulso para esquivar. Esc pausa; R solicita reiniciar el distrito y Enter confirma. M controla el sonido durante la aventura.

Comienza hablando con el personaje del refugio. Revisa el diario de la derecha para ver tus objetivos. En el cielo, inspecciona mensajes y llévalos al correo oficial o a cuarentena. En la selva reúne fragmentos y activa ambas defensas. Al atardecer desconecta estaciones y reporta al soporte. En la fortaleza usa cristales para encender balizas, rescata habitantes y activa el núcleo.

Tienes cinco unidades de energía. Evita los centinelas y las casillas brillantes. Si recibes daño vuelves al refugio conservando objetos, pero pierdes una energía y hasta 20 XP. Busca frutas reparadoras si te falta energía. Cada portal completado recupera una unidad. Con cero puedes reintentar el distrito o iniciar otra aventura.

Durante diálogos, pausa y resultados las amenazas no avanzan. La música se interrumpe durante los efectos y vuelve después. Cerrar la aplicación pierde la partida: el progreso se conserva solo durante la sesión.
''',
"documentacion/pensamiento_computacional.md": '''# Pensamiento computacional · Aventura 2D

| Componente | Evidencia en el juego |
|---|---|
| Descomposición | Mundos y datos, reglas, dibujo, audio, pruebas y documentación |
| Patrones | Los objetos comparten id, tipo y coordenadas; las misiones comparten refugio, objetivo y portal |
| Abstracción | La seguridad digital se representa con paquetes, llaves, balizas y conexiones; no se realizan ataques reales |
| Algoritmos | Colisiones por eje, validación de interacciones, secuencias de objetivos, avance y reinicio |

Variables: posición, energía, XP, nivel y radio. Listas: objetos y centinelas. Diccionarios: mapas y tipos de objetos. Conjuntos: objetivos terminados e inspecciones. Condicionales: requisitos de mecanismos y finales. Ciclos anidados: casillas del mapa y píxeles del personaje. Funciones/métodos: mover, escanear, interactuar, recibir_dano y cargar_nivel.

La prueba de accesibilidad usa una búsqueda en anchura sobre casillas transitables. Es una herramienta de validación de mapas y no una función artificial dentro del producto. Cada estructura responde a un problema concreto del mundo 2D.
''',
"documentacion/diseno_algoritmico.md": '''# Diseño algorítmico · Aventura 2D

## Bucle de juego

```text
iniciar ventana, fuentes, música y menú
mientras la ventana esté abierta:
    leer eventos: cierre, teclado y botones
    si hay partida y no hay pausa ni diálogo:
        actualizar temporizadores
        mover al jugador con subpasos y colisiones por eje
        mover centinelas entre sus extremos de patrulla
        detectar contacto con amenazas y peligros
    procesar notificaciones y animaciones
    dibujar mapa, personajes, objetos, diario y diálogos
    escalar imagen a la ventana y presentar
al salir: detener audio y liberar recursos
```

## Interactuar

```text
si existe diálogo: avanzar texto y terminar
si hay victoria o derrota: no actuar
buscar objeto más cercano a 51 píxeles o menos
rechazar si una pared corta el segmento hacia el objeto
si es personaje: activar misión y mostrar instrucciones
si no se habló con el personaje: solicitar conversación inicial
según tipo:
    mensaje: recoger si mochila vacía
    terminal: exigir mensaje inspeccionado y destino correcto
    forja: exigir tres fragmentos
    segundo factor: exigir forja y sello
    reporte: exigir tres estaciones desconectadas
    baliza: consumir un cristal
    habitante: exigir su baliza activa
    portal: exigir todos los objetivos; avanzar o ganar
marcar objetos completados y conceder su premio una sola vez
```

## Movimiento y daño

Se normaliza el vector de movimiento para que la diagonal no sea más rápida. El desplazamiento se divide en subpasos de hasta cinco píxeles; se comprueba el eje horizontal y después el vertical contra rectángulos de paredes. El impulso aumenta temporalmente la velocidad, sin omitir las colisiones.

Daño válido: energía menos uno, puntos menos 20 con mínimo cero, regreso al refugio y protección de 1,5 segundos. El reinicio restaura el estado de entrada al distrito y limpia sus objetivos. Los diálogos y la pausa congelan el mundo.

```mermaid
flowchart TD
    A[Menú y nombre] --> B[Introducción del distrito]
    B --> C[Explorar y hablar con personajes]
    C --> D[Recoger, inspeccionar y activar objetos]
    D --> E{Objetivos completos?}
    E -- No --> C
    E -- Sí --> F[Usar portal]
    F --> G{Último distrito?}
    G -- No --> B
    G -- Sí --> H[Victoria]
    C --> I{Energía cero?}
    I -- Sí --> J[Derrota o reintento]
```
''',
"documentacion/entrada_proceso_salida.md": '''# Entrada – Proceso – Salida

| Entrada | Proceso | Salida |
|---|---|---|
| Nombre | Validar 1–24 caracteres | Partida o aviso |
| Teclas de dirección y tiempo de frame | Normalizar, mover y comprobar paredes | Posición válida |
| E/Enter cerca de un personaje u objeto | Validar distancia, pared y requisitos | Diálogo, inventario, activación o bloqueo explicado |
| F | Inspeccionar objeto o paquete transportado | Evidencia y registro de inspección |
| H | Consumir llamada disponible | Orientación contextual |
| Espacio | Validar recarga | Impulso temporal |
| Contacto con peligro | Comprobar protección y aplicar daño | Energía, puntos y regreso al refugio |
| Portal completo | Registrar distrito y recuperar energía | Siguiente mapa o victoria |
| Reinicio confirmado | Restaurar instantánea de entrada | Distrito inicial sin recompensas acumuladas |
''',
"documentacion/diccionario_datos.md": '''# Diccionario de datos

| Dato | Tipo | Función y límites |
|---|---|---|
| nombre | str | 1–24 caracteres después de quitar espacios exteriores |
| x, y | float | Posición del personaje en píxeles del mapa |
| rect | pygame.Rect calculado | Área de colisión de 20 × 24 píxeles |
| energia | int | 0–5; cero indica derrota |
| puntos | int | No negativo; máximo sin daño 2700 |
| nivel | int | 0–3 |
| completadas | list[int] | Distritos terminados en orden |
| hechos | set[str] | Identificadores de objetivos u objetos usados en el distrito |
| inspeccionados | set[str] | Mensajes examinados con el escáner |
| carga | str o None | Identificador del único mensaje transportado |
| fragmentos, cristales | int | Recursos recogidos; cristales se consumen en balizas |
| sello | bool | Recuperación disponible para activar segundo factor |
| radio | int | 0–3 llamadas en la partida |
| dialogo | list[str] | Textos pendientes; detienen la simulación |
| invulnerable, impulso, espera_impulso | float | Segundos restantes de protección y recarga |
| muros | list[tuple[int,int]] | Casillas no transitables |
| objetos | list[dict] | id, tipo, x, y, nombre y requisitos |
| enemigos | list[dict] | Posición, dirección y extremos de patrulla |
| eventos | list[tuple[str,str]] | Mensaje de consecuencia y efecto sonoro |
| _inicio | tuple | Puntos, energía y radio al entrar al distrito |
''',
"documentacion/matriz_pruebas.md": '''# Matriz de pruebas · Aventura 2D

Verificación automatizada del 6 de noviembre de 2026 con Python 3.14.8 y pygame-ce 2.5.8.

| Caso | Resultado esperado | Resultado real |
|---|---|---|
| Nombre vacío o demasiado largo | Rechazo | Correcto en prueba automatizada |
| Movimiento hacia bordes | No atravesar paredes | Correcto |
| Accesibilidad de los mapas | Todos los objetos alcanzables por suelo seguro | Correcto mediante búsqueda en anchura |
| Campaña completa | Cuatro misiones completables por movimiento e interacción | Correcto con centinelas desactivados para determinismo |
| Portal incompleto | No avanzar | Correcto |
| Entrega sin inspección | Exigir escáner | Correcto |
| Repetición de entrega | No duplicar puntos | Correcto |
| Mecanismos fuera de orden | Rechazar sin premio | Correcto |
| Radio agotada y reinicio | No bajar de cero y restaurar estado de entrada | Correcto |
| Daño repetido durante protección | Una sola pérdida | Correcto |
| Derrota y reintento | Restaurar estado inicial del distrito | Correcto |
| Audio | Efecto sustituye fondo, retorno y silencio | Correcto con backend simulado |
| Menú, mapas, diálogos, pausa y finales | Renderizado y eventos válidos | Correcto con vídeo dummy |
| Dificultad con centinelas, claridad y sensación de control | Experiencia comprensible | Pendiente de prueba con personas |

Las pruebas deterministas de rutas no demuestran que una persona pueda superar las amenazas con facilidad. Se requiere una evaluación jugable real para equilibrar velocidad, energía y ubicación de peligros. Las capturas generadas son estados preparados del renderizador, no evidencia de evaluación con usuarios.
''',
"documentacion/presentacion.md": '''# Sustentación de la primera entrega · máximo 10 minutos

| Tiempo | Contenido |
|---|---|
| 0:00–1:00 | Problema local propuesto, público y evidencia recogida realmente |
| 1:00–2:00 | Propósito educativo y relación principal con ODS 4 |
| 2:00–3:00 | Design Thinking y decisiones de diseño; identificar investigación pendiente |
| 3:00–4:30 | Historia, personajes y cuatro distritos |
| 4:30–6:30 | Demostración: mover, hablar con Ada, recoger e inspeccionar un mensaje y entregarlo |
| 6:30–7:30 | Colisiones, inventario y objetivos como aplicación de programación |
| 7:30–8:30 | Storyboard, SVG y pruebas automatizadas |
| 8:30–9:30 | Tablero Kanban real, pendientes, aprendizajes y uso de IA |

Reservar 30 segundos de margen. La exposición es individual. La guía fija el 12 de noviembre durante la clase. No presentar las consultas o evaluaciones pendientes como realizadas.
''',
"documentacion/registro_mejoras.md": '''# Registro de mejoras

## 6 de noviembre de 2026 · Migración a aventura 2D

Tras la observación del docente y la solicitud del autor, se reemplazó el cuestionario por una aventura tradicional vista desde arriba. La interfaz activa utiliza Pygame y ofrece movimiento por teclado, colisiones, patrullas, diálogos, objetos, inventario y cuatro misiones espaciales.

Se conservaron las cuatro ambientaciones y la música original. Las ayudas de selección fueron sustituidas por escáner gratuito, radio de Ada con tres llamadas e impulso para esquivar. Los objetivos se validan en el mundo y los portales dependen de su finalización. El historial de la versión anterior se conserva en historial/prototipo_cuestionario; no es la aplicación activa.

Se verificaron rutas seguras hacia todos los objetos, campaña completa, restricciones de objetos, daño y reinicio. También se comprobaron renderizado y eventos sin ventana. La matriz identifica los límites de estas pruebas. Queda pendiente evaluar con personas la claridad, dificultad y utilidad educativa. No se atribuye aprobación docente a la nueva versión sin mostrársela.
''',
"documentacion/primera_entrega/contenido_adicional.md": '''# Portada y alcance

**CyberQuest: Los guardianes del escudo** · Institución Universitaria Antonio José Camacho · Ingeniería de Sistemas · Programación III · Tercer semestre.

**Autor:** Jorge Enrique Rentería Mosquera. Modalidad: individual. **Docente:** José Alejandro Martínez Pérez. Grupo: por completar.

**Actualización:** 6 de noviembre de 2026. **Sustentación:** 12 de noviembre, durante clase, máximo 10 minutos, según la imagen de la primera entrega. La imagen no especifica año; la planificación usa el año del curso.

## Cambio de propuesta

El docente solicitó una experiencia de juego tradicional con personajes, historia y gráficos 2D o 3D. La versión actual es una aventura 2D de exploración y objetivos espaciales: no hay selección de respuestas. Las instrucciones educativas se incorporan a diálogos, inspecciones y consecuencias de acciones realizadas en el mundo.

## Productos de esta entrega

| Producto | Evidencia actual | Pendiente |
|---|---|---|
| Análisis y ODS | Hipótesis, contexto propuesto y relación principal con ODS 4 | Evidencia local real |
| GDD | Historia, personajes, cuatro mapas y reglas de aventura | Revisión del docente y evaluación con personas |
| Storyboard | Secuencia de exploración, interacción y avance | Ajustes tras evaluación |
| Mockups | Menú, mapas 2D y diálogos en SVG | Evaluación de comprensión |
| Diseño algorítmico | Movimiento, colisiones, inventario y objetivos | Explicación oral del autor |
| Kanban | Tablero existente y CSV de migración preparado | Actualizar tablero y capturas fechadas |

# Storyboard de la aventura

| Viñeta | Pantalla y acción | Consecuencia |
|---|---|---|
| 1 | Menú: escribir nombre y comenzar | Crear personaje y entrar a las islas |
| 2 | Leer introducción y moverse hasta Ada | Conocer la amenaza y activar la misión |
| 3 | Recorrer senderos, evitar patrullas y recoger un paquete | Transportar un objeto en la mochila |
| 4 | Inspeccionar con F | Leer remitente, dominio y señales del mensaje |
| 5 | Alcanzar correo oficial o cuarentena y entregar con E | Consecuencia sobre progreso y puntos; una entrega insegura causa daño |
| 6 | Completar tres entregas y usar el portal | Entrar a la selva y recuperar una energía |
| 7 | Forjar llave, activar segundo factor y después contener estaciones | Resolver objetivos diferentes en nuevos mapas |
| 8 | Encender balizas, rescatar habitantes y activar el núcleo | Victoria y cierre de la historia |

## Diseño y accesibilidad

El mundo usa pixel art y paletas diferentes por distrito. El diario conserva objetivos y controles. Los diálogos pausan amenazas y no existe cuenta atrás. Los sonidos pueden silenciarse. La ventana se adapta manteniendo la proporción del mundo. Las herramientas se usan con teclas y tienen instrucciones visibles.

## Investigación y Design Thinking

Empatizar: consultar de forma voluntaria a 3–5 estudiantes, sin datos sensibles; pendiente. Definir: contrastar la hipótesis y priorizar necesidades; pendiente de esas consultas. Idear: se evaluó el alcance de un cuestionario y de una aventura, y se eligió la aventura ante la indicación del docente. Prototipar: cuatro mapas, reglas y gráficos implementados. Evaluar: pruebas automatizadas ejecutadas; evaluación con personas y balance pendientes.

| Participante anónimo | Fecha | Tarea o consulta | Hallazgo real | Cambio propuesto |
|---|---|---|---|---|
| P01 | Por completar | Explorar primer mapa | Pendiente de actividad | Por decidir |
| P02 | Por completar | Usar escáner y entregar mensaje | Pendiente de actividad | Por decidir |
| P03 | Por completar | Explicar el propósito del segundo factor | Pendiente de actividad | Por decidir |

## Relación con ODS

Se prioriza ODS 4, meta 4.4 e indicador de habilidades TIC, como alineación educativa propuesta. No se afirma que el juego mida el indicador ni produzca impacto demostrado. Fuente institucional consultada previamente: https://sdgs.un.org/goals/goal4. ODS 9 queda como relación contextual secundaria, sin atribuir avance medido en sus metas.

## Kanban y evidencia

El tablero CyberQuest existe en Notion: https://app.notion.com/p/190e3d2ac5714a58a4b651dd81806d15. Su existencia y 19 tarjetas se verificaron el 30 de octubre. Este paquete no implica que se haya actualizado el tablero tras la migración 2D. El CSV nuevo sirve para registrar estas tareas, con Jorge como responsable único.

Para la entrega: capturar la vista general, el detalle de una tarjeta con responsable/plazo/prioridad/evidencia y el historial real. Utilizar las cinco columnas de la guía. No inventar actividad histórica ni resultados de usuarios.

## Fuentes, recursos y declaración de IA

Fuentes del encargo: PDF original, imagen de primera entrega y observación del docente comunicada por el estudiante. Se utilizó Codex para programación, pruebas y borradores. Los gráficos y el audio son generados con código propio. Las capturas incluidas se obtuvieron del renderizador en estados iniciales preparados para documentación, sin simular que un usuario haya jugado. El autor debe comprender y declarar la asistencia según las orientaciones del curso.
''',
"documentacion/primera_entrega/LEEME.md": '''# Primera entrega · Aventura 2D

Versión actualizada el 6 de noviembre de 2026: CyberQuest es una aventura tradicional vista desde arriba. El código activo se ejecuta con `py main.py`, después de instalar requirements.txt.

Archivos: PDF para revisar/compartir, Word editable, HTML imprimible, ZIP del paquete, SVG de menú/mapas/diálogos, capturas PNG del renderizador y CSV de tareas de migración. Los SVG son mockups vectoriales. Las capturas PNG son imágenes del juego en estados iniciales preparados, no pruebas de evaluación con personas.

Pendientes: completar grupo, recoger evidencias locales del problema, evaluar claridad y dificultad con personas, mostrar el prototipo al docente y actualizar el tablero Notion con la migración. Sustentación indicada: 12 de noviembre, máximo 10 minutos durante clase. Trabajo individual de Jorge Enrique Rentería Mosquera.
''',
}


ACTUALIZACIONES = {
"README.md": '''
## Actualización del 9 de noviembre: enemigos y orientación

Los centinelas detectan al guardián por distancia y línea de visión. Muestran ! durante 0,55 segundos antes de perseguirlo, navegan por casillas sin atravesar paredes y recuerdan su última posición durante 2,2 segundos si dejan de verlo. Luego regresan a su zona. La velocidad de persecución aumenta por distrito: 128, 145, 160 y 178 píxeles/segundo; el guardián camina a 165 y puede usar el impulso para escapar. Las paredes sirven de cobertura. El refugio inicial está protegido y las amenazas no entran en él.

El diario indica el siguiente paso y el mapa marca los próximos tramos de una ruta segura entre paredes y peligros estáticos; no predice la posición de los centinelas. La guía gratuita T se puede consultar sin gastar radio. Los textos iniciales explican quién es el personaje y cómo continuar los diálogos. La radio H ofrece ayuda sobre el estado actual de la misión.

La verificación previa de persecución incluyó 15 pruebas unitarias, además de la comprobación gráfica, con pruebas de detección, cobertura, persecución en ambos ejes, retorno, refugio, dificultad progresiva y tutorial gratuito. Falta validar con jugadores el equilibrio de dificultad.
''',
"documentacion/GDD.md": '''
## Ajuste jugable del 9 de noviembre de 2026

Las amenazas emplean patrulla, alerta, persecución y regreso. Ven al jugador en un radio de 150 a 234 píxeles según el distrito, si no hay paredes entre ambos. La alerta visible dura 0,55 segundos. Persiguen en ambos ejes con navegación por casillas, recuerdan la última posición vista durante 2,2 segundos y regresan al origen al perder el rastro. La velocidad de persecución es 128/145/160/178 píxeles por segundo, frente a 165 del guardián. La fortaleza exige aprovechar cobertura e impulso. El refugio de entrada está protegido.

La introducción explica movimiento, diálogos y objetivo. El diario presenta el siguiente paso específico de cada estado, se resalta el destino y se muestran seis próximas casillas de ruta. Esta orientación evita paredes y peligros estáticos, pero no a las amenazas móviles. T abre una guía gratuita y H consume una llamada contextual. La evaluación de claridad y dificultad con personas sigue pendiente.
''',
"documentacion/manual_usuario.md": '''
## Cómo saber qué hacer

Tú eres el guardián de sombrero rojo. Pulsa E o Enter para cerrar cada texto; no puedes moverte mientras lees. Habla primero con el personaje del refugio. Revisa SIGUIENTE PASO en el diario y sigue las marcas doradas hasta el objeto resaltado. Las instrucciones cambian al recoger, inspeccionar, entregar o activar un mecanismo. T abre una explicación gratuita cuando la necesites. La radio H también explica tu siguiente acción.

## Cómo escapar de las amenazas

Un ! indica que te detectaron; tras una breve advertencia comenzará la persecución. Rompe la visión rodeando paredes, usa Espacio mientras te mueves para esquivar o vuelve al refugio marcado. Los centinelas recuerdan por poco tiempo dónde te vieron y después regresan a su zona. No entran en el refugio. Los últimos distritos tienen mayor alcance de detección y velocidad. Las marcas doradas guían entre obstáculos fijos: debes seguir esquivando las amenazas móviles.
''',
"documentacion/diseno_algoritmico.md": '''
## Centinelas y guía contextual

Cada centinela tiene estado, temporizador de alerta, memoria de última posición y ruta. Se calcula visión por distancia y por intersección del segmento hacia el jugador con las paredes. Al detectar se espera 0,55 segundos; luego se persigue la última posición conocida mediante búsqueda en anchura sobre casillas, excluyendo paredes, peligros y refugio. La ruta se recalcula cada 0,3 segundos o cuando cambia la casilla de destino. Al perder el rastro se vuelve al origen. También se validan colisiones rectangulares en cada eje del enemigo.

guia_actual consulta objetivos, inventario e inspecciones para devolver el siguiente objeto y una instrucción concreta. ruta_guia calcula una ruta evitando obstáculos fijos y el renderizador dibuja hasta seis casillas siguientes. Los diálogos y la pausa detienen la simulación de amenazas. El tutorial T no consume llamadas.
''',
"documentacion/registro_mejoras.md": '''
## 9 de noviembre de 2026 · Persecución y guía durante el juego

Se sustituyó la patrulla exclusivamente horizontal por detección con visión, alerta, persecución, memoria y regreso, con velocidades progresivas y refugio protegido. Se agregaron guía inicial, siguiente paso dinámico, resaltado del destino, ruta parcial y tutorial gratuito T. La radio ahora adapta su consejo al progreso actual. Pasaron 15 pruebas unitarias y la comprobación gráfica; se verificaron también el tutorial y su pausa. La valoración humana de dificultad y comprensión sigue pendiente.
''',
"documentacion/matriz_pruebas.md": '''
## Verificación adicional · 9 de noviembre de 2026

Verificación previa de persecución: 15 pruebas unitarias aprobadas y comprobación gráfica aprobada. Se añadieron pruebas de detección y advertencia, persecución con cambios de eje, bloqueo de visión por paredes, protección del refugio, pérdida de rastro y retorno sin atravesar obstáculos, mayor velocidad en lava, congelación durante diálogo, guía por estado y tutorial sin consumo de radio. Estas pruebas no sustituyen la evaluación humana del balance.
''',
"documentacion/primera_entrega/contenido_adicional.md": '''
## Actualización jugable del 9 de noviembre de 2026

Las amenazas detectan y persiguen al guardián con advertencia visual, cobertura y pérdida de rastro. El refugio está protegido. La guía inicial identifica al personaje y los controles; el diario muestra la acción inmediata, un destino resaltado y marcas de ruta. T abre ayuda gratuita y H da orientación contextual. Las capturas y SVG actuales muestran estas ayudas visuales. Falta evaluar con jugadores la dificultad y la comprensión.
''',
}
TABLA_DIFICULTAD = '''
## Selector de dificultad · 9 de noviembre de 2026

El menú permite elegir Fácil, Medio o Difícil con clic o con Tab antes de comenzar. Medio está seleccionado inicialmente. El modo queda fijo durante la partida, incluidos portales y reintentos; para cambiarlo se comienza otra aventura. Los objetivos, premios, diálogos, escáner gratuito, guía T y refugio protegido están disponibles en los tres modos.

| Parámetro | Fácil | Medio | Difícil |
|---|---|---|---|
| Energía inicial y máxima | 7 | 5 | 3 |
| Llamadas de radio por partida | 5 | 3 | 1 |
| Recuperación al completar distrito | Hasta 2 | Hasta 1 | Ninguna |
| Multiplicador de velocidad de patrulla y persecución | 0,75 | 1,00 | 1,18 |
| Multiplicador del alcance de visión | 0,80 | 1,00 | 1,15 |
| Advertencia antes de perseguir | 0,90 s | 0,55 s | 0,35 s |
| Memoria tras perder la visión | 1,4 s | 2,2 s | 3,2 s |
| Protección después del daño | 2,0 s | 1,5 s | 1,0 s |
| Recarga del impulso | 0,9 s | 1,2 s | 1,6 s |

Una fruta siempre recupera una unidad hasta el máximo de ese modo. Las velocidades base de persecución siguen aumentando entre los cuatro distritos (128, 145, 160 y 178 píxeles/segundo), multiplicadas por el modo. Así se distinguen la dificultad elegida de la progresión de la campaña. Los valores históricos de energía 5, radio 3 y recuperación 1 corresponden al modo Medio.

La configuración está centralizada en dificultad.py. Se verificaron valores iniciales, límites de frutas, persistencia y recuperación entre distritos, reinicio, velocidades y advertencias efectivas. La suite vigente tiene 19 pruebas unitarias aprobadas y comprobación gráfica aprobada; el balance con jugadores reales continúa pendiente.
'''
for nombre in ("README.md","documentacion/GDD.md","documentacion/manual_usuario.md","documentacion/matriz_pruebas.md","documentacion/primera_entrega/contenido_adicional.md"):
    DOCUMENTOS[nombre] += TABLA_DIFICULTAD
DOCUMENTOS["documentacion/registro_mejoras.md"] += "\n## Tres modos de dificultad\n\nSe incorporó un selector visible con Fácil, Medio y Difícil, configuración centralizada y modo persistente durante la campaña. Se parametrizaron energía, radio, recuperación, detección, movimiento enemigo, memoria, advertencia, protección y recarga. Pasaron 19 pruebas y la verificación gráfica del selector. La guía y el refugio siguen disponibles en todos los modos.\n"

for nombre,contenido in ACTUALIZACIONES.items():
    DOCUMENTOS[nombre] += contenido

if __name__ == "__main__":
    for nombre,contenido in DOCUMENTOS.items():
        (RAIZ/nombre).write_text(contenido,encoding="utf-8")
    print("Documentación actualizada a la aventura 2D.")
