# Manual de usuario

Ahora cada situación ofrece cuatro acciones. Examinar evidencia es gratis. Dispones para toda la partida de 3 pistas tácticas (−15 XP del premio), 2 comodines 50/50 (−25 XP) y 1 consulta a Ada (−40 XP). Úsalos antes de responder; puedes combinar tipos, pero no repetir un tipo en la misma situación. El 50/50 deshabilita dos acciones incorrectas. Las ayudas reducen solo el premio si aciertas: no gastan energía ni descuentan puntos al activarlas. El premio posible y los usos restantes aparecen en pantalla. Tras responder, la vista se desplaza hacia la explicación. El resumen final informa cuántas ayudas usaste.

La música relajante se reproduce automáticamente en bucle. Al acertar, perder energía u ocurrir otra acción con sonido, el efecto interrumpe el fondo. Después vuelve la música relajante desde el inicio del bucle. El botón SONIDO permite silenciar o activar todo el audio.

Cada misión cambia su paisaje y colores: 1) cielo con nubes, 2) selva, 3) cielo al atardecer, 4) fortaleza de lava. Son ambientaciones decorativas de la aventura digital; los botones y reglas funcionan de la misma manera. Al regresar al mapa se recupera el tema de ciudad cálida.

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
