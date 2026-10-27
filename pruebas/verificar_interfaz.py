"""Comprobación gráfica local: py pruebas/verificar_interfaz.py.

No reproduce audio ni sustituye una revisión visual y auditiva manual.
"""
from pathlib import Path
import sys
import tkinter as tk
import wave

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from interfaz import Aplicacion
from misiones import MISIONES


app = Aplicacion()
app.withdraw()
app.sonidos.activo = False
errores = []
app.report_callback_exception = lambda *error: errores.append(error)


def procesar():
    espera = tk.BooleanVar(app, False)
    app.after(120, espera.set, True)
    app.wait_variable(espera)


try:
    for ruta in app.sonidos.archivos.values():
        with wave.open(ruta) as sonido:
            assert sonido.getnchannels() == 1
            assert sonido.getnframes() > 0
    app.nombre.insert(0, "Prueba")
    app.comenzar()
    for nivel, mision in enumerate(MISIONES):
        app.abrir(nivel)
        for paso in range(len(mision["escenas"])):
            app.examinar(app.juego.escena_actual()["pista"])
            # Un error en el primer sector permite comprobar la recuperación.
            app.responder(1 if nivel == 0 and paso == 0 else 0)
            procesar()
            app.continuar()
            procesar()
    assert app.juego.victoria
    assert app.juego.energia == 3
    app.inicio()
    app.nombre.insert(0, "Derrota")
    app.comenzar()
    for nivel in range(2):
        app.abrir(nivel)
        for paso in range(2):
            app.responder(1)
            procesar()
            app.continuar()
    assert app.juego.derrota
    # Cambiar de pantalla cancela callbacks de widgets destruidos.
    for _ in range(8):
        app.inicio()
    procesar()
    assert not errores, errores
    print("OK: sonidos WAV, acierto, daño, recuperación, victoria, derrota y cancelación de animaciones.")
finally:
    app.destroy()
