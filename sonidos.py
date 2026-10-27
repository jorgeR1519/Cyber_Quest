"""Efectos arcade originales sintetizados; reproducción asíncrona en Windows."""
import math
from pathlib import Path
import struct
import tempfile
import wave

try:
    import winsound
except ImportError:
    winsound = None


MELODIAS = {
    "acierto": [(659, .08), (880, .08), (1175, .16)],
    "energia": [(523, .07), (784, .07), (1047, .07), (1397, .20)],
    "error": [(330, .12), (247, .12), (147, .24)],
    "abrir": [(440, .045), (660, .07)],
    "pista": [(1047, .045), (1319, .07)],
    "victoria": [(523, .10), (659, .10), (880, .10), (1175, .26)],
    "derrota": [(392, .14), (294, .14), (196, .16), (98, .30)],
}


class Sonidos:
    def __init__(self):
        self.activo = True
        self.temporal = tempfile.TemporaryDirectory(prefix="cyberquest_audio_")
        self.archivos = {}
        for nombre, notas in MELODIAS.items():
            ruta = Path(self.temporal.name) / f"{nombre}.wav"
            datos = bytearray()
            for frecuencia, duracion in notas:
                cantidad = int(22050 * duracion)
                for i in range(cantidad):
                    # Onda cuadrada suave con ataque y caída para evitar chasquidos.
                    envolvente = min(1, i / 180, (cantidad - i) / 350)
                    onda = 1 if math.sin(2 * math.pi * frecuencia * i / 22050) >= 0 else -1
                    datos.extend(struct.pack("<h", int(onda * 2700 * envolvente)))
            with wave.open(str(ruta), "wb") as archivo:
                archivo.setparams((1, 2, 22050, 0, "NONE", "not compressed"))
                archivo.writeframes(datos)
            self.archivos[nombre] = str(ruta)

    def tocar(self, nombre):
        if self.activo and winsound:
            try:
                winsound.PlaySound(self.archivos[nombre], winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
            except RuntimeError:
                pass  # Un dispositivo de audio no disponible no interrumpe la partida.

    def cerrar(self):
        if winsound:
            winsound.PlaySound(None, 0)
        self.temporal.cleanup()
