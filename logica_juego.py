"""Reglas independientes de Tkinter, para poder probarlas sin ventanas."""
from misiones import MISIONES


class Juego:
    ENERGIA_MAXIMA = 3

    def __init__(self, nombre):
        nombre = nombre.strip()
        if not 1 <= len(nombre) <= 24:
            raise ValueError("Escribe un nombre de 1 a 24 caracteres.")
        self.nombre = nombre
        self.puntos = 0
        self.energia = self.ENERGIA_MAXIMA
        self.completadas = []
        self.nivel = None
        self.paso = 0
        self.pendiente = False
        self.historial = []
        self._inicio = None

    @property
    def derrota(self):
        return self.energia == 0

    @property
    def victoria(self):
        return len(self.completadas) == len(MISIONES) and not self.derrota

    def iniciar_mision(self, nivel):
        if self.derrota or self.victoria:
            raise ValueError("La partida terminó. Inicia una nueva partida.")
        if type(nivel) is not int or nivel != len(self.completadas):
            raise ValueError("Esta misión está bloqueada o ya fue completada.")
        if self.nivel is not None:
            raise ValueError("Ya hay una misión activa.")
        self.nivel = nivel
        self.paso = 0
        self.pendiente = False
        self._inicio = (self.puntos, self.energia, len(self.historial))

    def escena_actual(self):
        if self.nivel is None or self.derrota or self.victoria:
            raise ValueError("No hay una misión activa.")
        return MISIONES[self.nivel]["escenas"][self.paso]

    def decidir(self, opcion):
        escena = self.escena_actual()
        if self.pendiente:
            raise ValueError("Lee la retroalimentación y continúa.")
        if type(opcion) is not int or not 0 <= opcion < len(escena["opciones"]):
            raise ValueError("Selecciona una acción válida.")
        accion = escena["opciones"][opcion]
        if accion["segura"]:
            self.puntos += 100
        else:
            self.puntos = max(0, self.puntos - 50)
            self.energia = max(0, self.energia - 1)
        self.pendiente = True
        resultado = {"nivel": self.nivel, "paso": self.paso,
                     "segura": accion["segura"], "explicacion": accion["explicacion"]}
        self.historial.append(resultado)
        return resultado

    def continuar(self):
        if self.derrota or not self.pendiente:
            raise ValueError("No puedes avanzar en este momento.")
        self.pendiente = False
        self.paso += 1
        if self.paso == len(MISIONES[self.nivel]["escenas"]):
            self.completadas.append(self.nivel)
            self.nivel = None
            self.paso = 0
            self.energia = min(self.ENERGIA_MAXIMA, self.energia + 1)
            return "victoria" if self.victoria else "completada"
        return "escena"

    def reiniciar_mision(self):
        if self.nivel is None or self.derrota:
            raise ValueError("Reinicia la partida desde la pantalla final.")
        self.puntos, self.energia, largo = self._inicio
        del self.historial[largo:]
        self.paso = 0
        self.pendiente = False
