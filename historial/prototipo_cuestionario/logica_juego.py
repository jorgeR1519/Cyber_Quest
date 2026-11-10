"""Reglas independientes de Tkinter, para poder probarlas sin ventanas."""
from misiones import MISIONES
import random


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
        self.ayudas = {"pista": 3, "descarte": 2, "mentor": 1}
        self.ayudas_escena = []
        self.descartadas = []

    @property
    def recompensa(self):
        costes = {"pista": 15, "descarte": 25, "mentor": 40}
        return 100 - sum(costes[ayuda] for ayuda in self.ayudas_escena)

    def usar_ayuda(self, tipo):
        escena = self.escena_actual()
        if self.pendiente:
            raise ValueError("Las ayudas se utilizan antes de responder.")
        if tipo not in self.ayudas or self.ayudas[tipo] <= 0:
            raise ValueError("No quedan usos de esta ayuda en la partida.")
        if tipo in self.ayudas_escena:
            raise ValueError("Ya usaste esta ayuda en esta situación.")
        self.ayudas[tipo] -= 1
        self.ayudas_escena.append(tipo)
        if tipo == "descarte":
            candidatas = [i for i, opcion in enumerate(escena["opciones"]) if not opcion["segura"]]
            self.descartadas = random.sample(candidatas, 2)
            return "50/50: se descartaron dos acciones riesgosas. Aún debes analizar las dos restantes."
        if tipo == "mentor":
            return "Mentora Ada: " + escena["opciones"][0]["explicacion"]
        return "Pista táctica: " + escena["consejo"]

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
        self.ayudas_escena = []
        self.descartadas = []
        self._inicio = (self.puntos, self.energia, len(self.historial), self.ayudas.copy())

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
        if opcion in self.descartadas:
            raise ValueError("Esta acción fue descartada por el comodín 50/50.")
        accion = escena["opciones"][opcion]
        if accion["segura"]:
            self.puntos += self.recompensa
        else:
            self.puntos = max(0, self.puntos - 50)
            self.energia = max(0, self.energia - 1)
        self.pendiente = True
        resultado = {"nivel": self.nivel, "paso": self.paso,
                     "segura": accion["segura"], "explicacion": accion["explicacion"],
                     "ayudas": self.ayudas_escena.copy(), "premio": self.recompensa if accion["segura"] else 0}
        self.historial.append(resultado)
        return resultado

    def continuar(self):
        if self.derrota or not self.pendiente:
            raise ValueError("No puedes avanzar en este momento.")
        self.pendiente = False
        self.paso += 1
        self.ayudas_escena = []
        self.descartadas = []
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
        self.puntos, self.energia, largo, ayudas = self._inicio
        self.ayudas = ayudas.copy()
        self.ayudas_escena = []
        self.descartadas = []
        del self.historial[largo:]
        self.paso = 0
        self.pendiente = False
