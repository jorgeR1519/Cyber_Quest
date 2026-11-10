"""Prueba del renderizado y eventos, sin ventana visible ni sonido."""
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import pygame as pg
from aventura import Aplicacion

app = Aplicacion(audio=False)
try:
    app.dibujar(); app.presentar()
    for modo in ("facil","medio","dificil"):
        app.elegir_dificultad(modo); app.dibujar()
    app.manejar_evento(pg.event.Event(pg.KEYDOWN,key=pg.K_TAB,unicode="\t"))
    assert app.dificultad == "facil"
    app.elegir_dificultad("medio")
    app.nombre = "Prueba"; app.iniciar()
    for nivel in range(4):
        app.juego.nivel = nivel; app.juego.cargar_nivel()
        app.dibujar(); app.presentar()
        while app.juego.dialogo:
            app.manejar_evento(pg.event.Event(pg.KEYDOWN,key=pg.K_e,unicode="e"))
        app.actualizar(.016); app.dibujar()
        app.manejar_evento(pg.event.Event(pg.KEYDOWN,key=pg.K_t,unicode="t"))
        assert app.juego.dialogo and app.juego.radio == 3
        app.dibujar()
        while app.juego.dialogo:
            app.juego.interactuar()
        app.manejar_evento(pg.event.Event(pg.KEYDOWN,key=pg.K_ESCAPE,unicode=""))
        assert app.pausa
        app.dibujar()
        app.manejar_evento(pg.event.Event(pg.KEYDOWN,key=pg.K_ESCAPE,unicode=""))
        assert not app.pausa
        app.juego.escanear(); app.dibujar()
    app.juego.victoria = True; app.dibujar()
    app.juego.victoria = False; app.juego.energia = 0; app.dibujar()
    app.manejar_evento(pg.event.Event(pg.KEYDOWN,key=pg.K_r,unicode="r"))
    assert app.juego.energia > 0
    app.manejar_evento(pg.event.Event(pg.QUIT))
    assert app.salir
    print("OK: menú, cuatro mundos, diálogos, pausa, victoria, derrota, reinicio y cierre.")
finally:
    app.cerrar()
