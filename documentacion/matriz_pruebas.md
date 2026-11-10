# Matriz de pruebas · Aventura 2D

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

## Verificación adicional · 9 de noviembre de 2026

Verificación previa de persecución: 15 pruebas unitarias aprobadas y comprobación gráfica aprobada. Se añadieron pruebas de detección y advertencia, persecución con cambios de eje, bloqueo de visión por paredes, protección del refugio, pérdida de rastro y retorno sin atravesar obstáculos, mayor velocidad en lava, congelación durante diálogo, guía por estado y tutorial sin consumo de radio. Estas pruebas no sustituyen la evaluación humana del balance.
