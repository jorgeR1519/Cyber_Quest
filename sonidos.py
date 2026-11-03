"""Música relajante y efectos originales, con un único canal de audio."""
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
    def __init__(self, programador):
        self.programador = programador
        self._activo = True
        self.cerrado = False
        self.reanudacion = None
        self.duraciones = {}
        self.temporal = tempfile.TemporaryDirectory(prefix="cyberquest_audio_")
        self.archivos = {}
        for nombre, notas in MELODIAS.items():
            self.duraciones[nombre] = sum(duracion for _, duracion in notas)
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
        self.crear_fondo()

    def crear_fondo(self):
        """Arpegio lento de ondas suaves, a menor volumen que los efectos."""
        ruta = Path(self.temporal.name) / "fondo.wav"
        datos = bytearray()
        # Progresión original en do mayor, sin grabaciones ni descargas.
        acordes = [(261.63, 329.63, 392.00), (220.00, 261.63, 329.63),
                   (174.61, 220.00, 261.63), (196.00, 246.94, 293.66)]
        muestras = 22050
        for acorde in acordes:
            for nota in (acorde[0], acorde[1], acorde[2], acorde[1]):
                cantidad = int(muestras * .8)
                for i in range(cantidad):
                    t = i / muestras
                    envolvente = math.sin(math.pi*i/cantidad)**2
                    melodia = math.sin(2*math.pi*nota*t) + .15*math.sin(4*math.pi*nota*t)
                    bajo = .25*math.sin(2*math.pi*(acorde[0]/2)*t)
                    datos.extend(struct.pack("<h", int((melodia+bajo)*1000*envolvente)))
        with wave.open(str(ruta), "wb") as archivo:
            archivo.setparams((1, 2, muestras, 0, "NONE", "not compressed"))
            archivo.writeframes(datos)
        self.archivos["fondo"] = str(ruta)

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, valor):
        self._activo = bool(valor)
        self.cancelar_reanudacion()
        if not self._activo:
            self.detener()
        elif not self.cerrado:
            self.iniciar_fondo()

    def cancelar_reanudacion(self):
        if self.reanudacion is not None:
            self.programador.after_cancel(self.reanudacion)
            self.reanudacion = None

    def detener(self):
        if winsound:
            try:
                winsound.PlaySound(None, 0)
            except RuntimeError:
                pass

    def iniciar_fondo(self):
        self.reanudacion = None
        if self.activo and not self.cerrado and winsound:
            try:
                winsound.PlaySound(self.archivos["fondo"], winsound.SND_FILENAME |
                                   winsound.SND_ASYNC | winsound.SND_LOOP | winsound.SND_NODEFAULT)
            except RuntimeError:
                pass

    def tocar(self, nombre):
        if self.activo and not self.cerrado and winsound:
            self.cancelar_reanudacion()
            try:
                # PlaySound sustituye el fondo: nunca se mezclan ambos audios.
                winsound.PlaySound(self.archivos[nombre], winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
            except RuntimeError:
                pass  # Un dispositivo de audio no disponible no interrumpe la partida.
            self.reanudacion = self.programador.after(
                int(self.duraciones[nombre]*1000)+50, self.iniciar_fondo)

    def cerrar(self):
        self.cerrado = True
        self.cancelar_reanudacion()
        self.detener()
        self.temporal.cleanup()
