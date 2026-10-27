# CyberQuest: Defensa Digital

Videojuego educativo para Programación III. Python y Tkinter; cuatro misiones, nueve decisiones y gráficos dibujados con Canvas. Funciona localmente sin internet ni paquetes externos.

## Ejecutar en Windows

Instala Python 3.10 o posterior con el componente Tcl/Tk. Desde esta carpeta:

```powershell
py main.py
```

Si tu instalación usa `python`, reemplaza `py` por `python`. Para comprobar Tkinter: `py -m tkinter`.

## Pruebas

```powershell
py -m unittest discover -s pruebas -v
```

Las pruebas cubren reglas del juego; la navegación y distribución visual necesitan una revisión manual. Consulta `documentacion/matriz_pruebas.md` para registrar los resultados reales.

## Archivos para estudiar

- `misiones.py`: datos narrativos y consecuencias educativas.
- `logica_juego.py`: estado, validación, puntuación, progreso y reinicio.
- `interfaz.py`: pantallas, botones y dibujo de la ciudad.
- `main.py`: punto de entrada.
- `documentacion/`: diseño, metodología, manual y preparación de la entrega.

## Reglas

La interfaz utiliza fondo crema, tonos cálidos de melocotón y terracota, y texto oscuro. Una ciudad de pixel art incluye un guardián animado, un corazón flotante y nubes en movimiento, dibujados con Canvas. Conserva confeti de píxeles y animaciones de respuesta. Incluye efectos arcade originales para aciertos, daño, recuperación de energía y finales (no son grabaciones ni melodías de Mario). El botón SONIDO permite silenciarlos. La reproducción utiliza `winsound` en Windows; en otros sistemas el juego funciona sin audio. No se requieren paquetes externos. Las animaciones se cancelan al cambiar de pantalla y el contenido permite desplazamiento vertical.

Comprobación adicional de interfaz y archivos de sonido: `py pruebas/verificar_interfaz.py`. Esta comprobación automatizada no evalúa cómo se ve o escucha en tu equipo.

Nombre de 1 a 24 caracteres tras quitar espacios exteriores. Energía inicial 3, rango 0–3. Decisión segura +100 XP; riesgosa −50 XP sin bajar de 0 y −1 energía. Completar una misión recupera 1 energía. Se avanza después de leer la explicación y pulsar Continuar. Una misión se completa al resolver todas sus escenas con energía restante; puede contener errores. Cero energía causa derrota inmediata. Completar las cuatro misiones causa victoria. Máximo 900 XP.

Solo se puede jugar la siguiente misión pendiente. Reiniciar una misión restaura puntos, energía e historial a su inicio. Después de perder se inicia otra partida. El progreso vive en memoria y se pierde al cerrar.

## Estado de la entrega

Código y documentos iniciales preparados. Se ejecutaron cinco pruebas automatizadas con Python 3.14.8: todas pasaron. También se comprobó la creación de la interfaz Tkinter y una secuencia de navegación programática. Sigue pendiente la revisión visual e interacción completa por una persona. El tablero digital, video y evidencias de campo siguen pendientes.

La guía del profesor solicita trabajo en equipo; el documento de contexto plantea trabajo individual. Confirma con el docente la modalidad autorizada antes de presentar la entrega.

Se utilizó asistencia de IA (Codex) para generar código, pruebas y borradores. El estudiante debe revisar, comprender y adaptar el material y declarar su uso según las orientaciones del curso. Los escenarios son ficticios y los dibujos se crean con código, sin recursos gráficos externos.
