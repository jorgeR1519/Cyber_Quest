# Portada y alcance

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

## Actualización jugable del 9 de noviembre de 2026

Las amenazas detectan y persiguen al guardián con advertencia visual, cobertura y pérdida de rastro. El refugio está protegido. La guía inicial identifica al personaje y los controles; el diario muestra la acción inmediata, un destino resaltado y marcas de ruta. T abre ayuda gratuita y H da orientación contextual. Las capturas y SVG actuales muestran estas ayudas visuales. Falta evaluar con jugadores la dificultad y la comprensión.
