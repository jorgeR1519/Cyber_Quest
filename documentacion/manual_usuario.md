# Manual de usuario · Aventura 2D

Instala las dependencias con `py -m pip install -r requirements.txt` y ejecuta `py main.py`. Escribe un nombre y pulsa Enter o Comenzar aventura.

Muévete con WASD o flechas. E/Enter habla con personajes, recoge objetos, activa mecanismos y continúa textos. F inspecciona un objeto cercano o el mensaje transportado. H solicita una de las tres ayudas por radio. Espacio mientras te mueves activa el impulso para esquivar. Esc pausa; R solicita reiniciar el distrito y Enter confirma. M controla el sonido durante la aventura.

Comienza hablando con el personaje del refugio. Revisa el diario de la derecha para ver tus objetivos. En el cielo, inspecciona mensajes y llévalos al correo oficial o a cuarentena. En la selva reúne fragmentos y activa ambas defensas. Al atardecer desconecta estaciones y reporta al soporte. En la fortaleza usa cristales para encender balizas, rescata habitantes y activa el núcleo.

Tienes cinco unidades de energía. Evita los centinelas y las casillas brillantes. Si recibes daño vuelves al refugio conservando objetos, pero pierdes una energía y hasta 20 XP. Busca frutas reparadoras si te falta energía. Cada portal completado recupera una unidad. Con cero puedes reintentar el distrito o iniciar otra aventura.

Durante diálogos, pausa y resultados las amenazas no avanzan. La música se interrumpe durante los efectos y vuelve después. Cerrar la aplicación pierde la partida: el progreso se conserva solo durante la sesión.

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

## Cómo saber qué hacer

Tú eres el guardián de sombrero rojo. Pulsa E o Enter para cerrar cada texto; no puedes moverte mientras lees. Habla primero con el personaje del refugio. Revisa SIGUIENTE PASO en el diario y sigue las marcas doradas hasta el objeto resaltado. Las instrucciones cambian al recoger, inspeccionar, entregar o activar un mecanismo. T abre una explicación gratuita cuando la necesites. La radio H también explica tu siguiente acción.

## Cómo escapar de las amenazas

Un ! indica que te detectaron; tras una breve advertencia comenzará la persecución. Rompe la visión rodeando paredes, usa Espacio mientras te mueves para esquivar o vuelve al refugio marcado. Los centinelas recuerdan por poco tiempo dónde te vieron y después regresan a su zona. No entran en el refugio. Los últimos distritos tienen mayor alcance de detección y velocidad. Las marcas doradas guían entre obstáculos fijos: debes seguir esquivando las amenazas móviles.
