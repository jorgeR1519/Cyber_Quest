"""Capturas reales del renderizador en estados iniciales preparados, sin jugar por el usuario."""
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"
from pathlib import Path
import sys
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(RAIZ))
import pygame as pg
from aventura import Aplicacion


def capturar(destino):
    app = Aplicacion(audio=False)
    try:
        app.nombre = "Guardián"
        app.dibujar(); pg.image.save(app.lienzo,str(destino/"captura_menu.png"))
        app.iniciar()
        for nivel in range(4):
            app.juego.nivel = nivel; app.juego.cargar_nivel()
            app.juego.dialogo = []
            app.noticia = app.juego.mision["objetivo"]
            app.noticia_hasta = app.tiempo+10
            app.dibujar(); pg.image.save(app.lienzo,str(destino/f"captura_mision_{nivel+1}.png"))
            app.juego.dialogo = [app.juego.mision["dialogo"]]
            app.dibujar(); pg.image.save(app.lienzo,str(destino/f"captura_dialogo_{nivel+1}.png"))
    finally:
        app.cerrar()


if __name__ == "__main__":
    capturar(RAIZ/"documentacion"/"primera_entrega")
