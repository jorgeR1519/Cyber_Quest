"""Navegación por casillas y centinelas con visión, memoria y persecución."""
from collections import deque
import math
import pygame
from mundos import ANCHO, ALTO


def buscar_ruta(inicio, destino, bloqueadas):
    if destino in bloqueadas:
        return []
    pendientes = deque([inicio]); anteriores = {inicio: None}
    while pendientes:
        actual = pendientes.popleft()
        if actual == destino:
            camino = []
            while actual != inicio:
                camino.append(actual); actual = anteriores[actual]
            return camino[::-1]
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            vecino = actual[0]+dx,actual[1]+dy
            if 0 <= vecino[0] < ANCHO and 0 <= vecino[1] < ALTO and vecino not in bloqueadas and vecino not in anteriores:
                anteriores[vecino] = actual; pendientes.append(vecino)
    return []


def actualizar_centinela(juego, enemigo, dt):
    e = enemigo
    for clave,valor in dict(estado="patrulla",aviso=0.,memoria=0.,recalcular=0.,ruta=[],meta=None,
                            origen_y=e["y"],visto=(e["x"],e["y"])).items():
        e.setdefault(clave,valor)
    centro = (e["x"]+11,e["y"]+11)
    jugador = juego.rect.center
    refugio = juego.en_refugio()
    bloqueadas = set(juego.muros+juego.mision["peligros"])
    bloqueadas.update((x,y) for x in range(1,5) for y in range(1,4))
    visible = not refugio and math.dist(centro,jugador) <= (150+juego.nivel*28)*juego.config["vision"] and not any(
        pygame.Rect(x*32,y*32,32,32).clipline(centro,jugador) for x,y in juego.muros)
    if visible:
        e["visto"] = juego.x,juego.y; e["memoria"] = juego.config["memoria"]
        if e["estado"] in ("patrulla","regreso"):
            e["estado"] = "alerta"; e["aviso"] = juego.config["aviso"]; e["ruta"] = []; e["recalcular"] = 0
    else:
        e["memoria"] = max(0,e["memoria"]-dt)
    if refugio or (e["estado"] in ("alerta","persigue") and not e["memoria"]):
        e["estado"] = "regreso"
    if e["estado"] == "alerta":
        e["aviso"] = max(0,e["aviso"]-dt)
        if not e["aviso"]:
            e["estado"] = "persigue"; e["recalcular"] = 0
        return
    if e["estado"] == "persigue":
        destino = e["visto"]
        velocidad = (128,145,160,178)[juego.nivel]*juego.config["velocidad"]
    elif e["estado"] == "regreso":
        destino = e["inicio"],e["origen_y"]
        velocidad = 90
        if math.dist((e["x"],e["y"]),destino) < 3:
            e["estado"] = "patrulla"; e["recalcular"] = 0
    else:
        destino = (e["fin"] if e["direccion"] == 1 else e["inicio"],e["origen_y"])
        velocidad = (65+juego.nivel*9)*juego.config["velocidad"]
        if math.dist((e["x"],e["y"]),destino) < 3:
            e["direccion"] *= -1
            destino = (e["fin"] if e["direccion"] == 1 else e["inicio"],e["origen_y"])
    casilla = int((e["x"]+11)//32),int((e["y"]+11)//32)
    meta = int((destino[0]+10)//32),int((destino[1]+12)//32)
    e["recalcular"] -= dt
    if meta != e["meta"] or e["recalcular"] <= 0:
        e["ruta"] = buscar_ruta(casilla,meta,bloqueadas)
        e["meta"] = meta; e["recalcular"] = .3
    if e["ruta"]:
        x,y = e["ruta"][0]; objetivo = x*32+5,y*32+5
        if math.dist((e["x"],e["y"]),objetivo) < 2:
            e["ruta"].pop(0)
    elif casilla == meta:
        objetivo = destino
    else:
        return
    dx,dy = objetivo[0]-e["x"],objetivo[1]-e["y"]
    distancia = math.hypot(dx,dy)
    if not distancia:
        return
    paso = min(velocidad*dt,distancia)
    nx,ny = e["x"]+dx/distancia*paso,e["y"]+dy/distancia*paso
    # Colisiones también para las amenazas: ninguna atraviesa paredes ni el refugio.
    def libre(x,y):
        rect = pygame.Rect(round(x),round(y),23,23)
        return not any(rect.colliderect(pygame.Rect(a*32,b*32,32,32)) for a,b in bloqueadas)
    if libre(nx,e["y"]): e["x"] = nx
    if libre(e["x"],ny): e["y"] = ny
