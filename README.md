# CyberQuest: Los guardianes del escudo

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

Recoger fragmentos, sellos y cristales concede 25 XP. Entregas correctas, mecanismos, estaciones, reportes, balizas y rescates conceden 100 XP. Completar un distrito concede 200 XP y recupera una energía hasta 5. Las frutas recuperan una energía y no se consumen si ya está completa. No se repiten recompensas de objetos usados. El máximo de una partida sin daño es 2475 XP.

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

## Actualización del 9 de noviembre: enemigos y orientación

Los centinelas detectan al guardián por distancia y línea de visión. Muestran ! durante 0,55 segundos antes de perseguirlo, navegan por casillas sin atravesar paredes y recuerdan su última posición durante 2,2 segundos si dejan de verlo. Luego regresan a su zona. La velocidad de persecución aumenta por distrito: 128, 145, 160 y 178 píxeles/segundo; el guardián camina a 165 y puede usar el impulso para escapar. Las paredes sirven de cobertura. El refugio inicial está protegido y las amenazas no entran en él.

El diario indica el siguiente paso y el mapa marca los próximos tramos de una ruta segura entre paredes y peligros estáticos; no predice la posición de los centinelas. La guía gratuita T se puede consultar sin gastar radio. Los textos iniciales explican quién es el personaje y cómo continuar los diálogos. La radio H ofrece ayuda sobre el estado actual de la misión.

La verificación previa de persecución incluyó 15 pruebas unitarias, además de la comprobación gráfica, con pruebas de detección, cobertura, persecución en ambos ejes, retorno, refugio, dificultad progresiva y tutorial gratuito. Falta validar con jugadores el equilibrio de dificultad.
