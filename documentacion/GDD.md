# GDD · CyberQuest: Los guardianes del escudo

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

Fragmentos, sello y cristales: +25 XP. Objetivos de entrega, forja, segundo factor, estaciones, reporte, balizas y rescates: +100 XP. Completar distrito: +200 XP y +1 energía hasta el máximo. Máximo sin daño: 2475 XP. La recompensa de cada objeto solo se obtiene una vez. El escáner es gratuito y la radio dispone de tres llamadas por partida.

El primer distrito exige haber inspeccionado el mensaje antes de entregarlo. Una terminal incorrecta causa daño y conserva el paquete para corregir la acción. La forja requiere tres fragmentos; el segundo factor requiere la forja y el sello. El reporte requiere tres estaciones desconectadas. Cada rescate requiere su baliza activa; cada baliza consume un cristal. El portal final exige las tres balizas y tres rescates.

## Avance y finales

Se habla con el personaje del refugio antes de activar objetivos. Los portales se abren solo al terminar la misión. Victoria: activar el núcleo al completar los cuatro distritos. Derrota: energía cero. Reiniciar restaura el estado de entrada al distrito, incluidas las llamadas y los puntos, conservando el avance de distritos anteriores. Empezar otra aventura reinicia todo. No hay guardado persistente.

## Estética, sonido y narrativa

Pixel art dibujado con formas propias: personaje animado, tiles, objetos flotantes y centinelas con alas. Cada distrito utiliza una paleta completa. La música original relajante se reproduce en bucle; los efectos la interrumpen y el fondo vuelve al terminar. Se puede silenciar. La información importante también se comunica por texto.

## Navegación

Menú y nombre → introducción → exploración → interacción y diálogos → objetivo completo → portal → siguiente distrito → victoria. Daño puede llevar a derrota; pausa permite reiniciar con confirmación. El storyboard y los SVG actuales se encuentran en la carpeta de primera entrega.

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

## Ajuste jugable del 9 de noviembre de 2026

Las amenazas emplean patrulla, alerta, persecución y regreso. Ven al jugador en un radio de 150 a 234 píxeles según el distrito, si no hay paredes entre ambos. La alerta visible dura 0,55 segundos. Persiguen en ambos ejes con navegación por casillas, recuerdan la última posición vista durante 2,2 segundos y regresan al origen al perder el rastro. La velocidad de persecución es 128/145/160/178 píxeles por segundo, frente a 165 del guardián. La fortaleza exige aprovechar cobertura e impulso. El refugio de entrada está protegido.

La introducción explica movimiento, diálogos y objetivo. El diario presenta el siguiente paso específico de cada estado, se resalta el destino y se muestran seis próximas casillas de ruta. Esta orientación evita paredes y peligros estáticos, pero no a las amenazas móviles. T abre una guía gratuita y H consume una llamada contextual. La evaluación de claridad y dificultad con personas sigue pendiente.
