# Manual de usuario

1. Abre una terminal en la carpeta del proyecto y ejecuta `py main.py` con Python y Tkinter instalados.
2. Escribe un nombre de 1 a 24 caracteres y pulsa Comenzar aventura.
3. Abre el primer sector disponible en el mapa.
4. Lee el incidente y pulsa Examinar evidencia para ver sus señales.
5. Elige una acción. Lee su consecuencia y pulsa Continuar.
6. Completa las situaciones para desbloquear el siguiente sector. Al terminar una misión recuperas una unidad de energía, hasta 3.
7. Protege los cuatro sectores para ganar. Si la energía llega a 0, la partida termina y puedes volver a jugar.

Cada acción segura da 100 XP; cada riesgo resta 50 XP y una energía. Los puntos no bajan de 0. Puedes reiniciar una misión activa para restaurar el estado de su inicio. Después de perder debes iniciar otra partida. Nueva partida solicita confirmación cuando abandona el progreso desde el mapa.

El juego funciona sin internet. No introduzcas contraseñas ni datos reales. No guarda progreso: cerrar la ventana termina la sesión.

La interfaz tiene colores cálidos y una ciudad de pixel art con un guardián, un corazón y nubes animadas. Los rombos representan la energía disponible. Cada decisión muestra confeti de píxeles; el daño se distingue por una alerta roja y el texto de pérdida de energía. Al completar un sector se anuncia si recuperaste energía o ya estabas al máximo. Los efectos de audio son melodías arcade originales y se reproducen en Windows. Usa SONIDO: ON/OFF en la barra superior para silenciarlos. Puedes desplazar el contenido con la rueda del ratón o la barra lateral.

Si `py` no existe, prueba `python main.py` en una instalación de Python válida. Si falta Tkinter, modifica la instalación de Python para incluir Tcl/Tk. Para comprobarlo ejecuta `py -m tkinter`.
