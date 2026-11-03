"""Mockups SVG por misión, basados en el contenido y los dibujos del juego."""
from html import escape
from textwrap import wrap

from misiones import MISIONES
from temas import TEMAS, paisaje, ambiente


def mockup(tipo, nivel=0):
    tema, mision = TEMAS[nivel], MISIONES[nivel]
    escena = mision["escenas"][0]
    retro = tipo == "retroalimentacion"
    partes = []
    def caja(x, y, w, h, color):
        partes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>')
    def texto(x, y, contenido, tam=18, color=None):
        partes.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" font-size="{tam}" fill="{color or tema["texto"]}">{escape(contenido)}</text>')
    def parrafo(contenido, y, tam=18, ancho=83, color=None):
        lineas = wrap(contenido, ancho)
        for linea in lineas:
            texto(40, y, linea, tam, color)
            y += tam+7
        return y
    caja(0, 0, 900, 1400, tema["panel"])
    caja(0, 0, 900, 46, tema["panel"])
    texto(24, 29, "CYBERQUEST · Defensa Digital", 19)
    texto(750, 29, "Sonido: ON", 15)
    texto(40, 88, mision["titulo"], 27)
    texto(40, 119, f"{tema['nombre']}  ·  Misión {nivel+1} de 4", 17, tema["acento"])
    texto(40, 148, f"Guardián: Ada  |  XP: {100 if retro else 0}  |  Energía: 3/3", 16)
    partes.append('<g transform="translate(40 168) scale(0.911111 1)">')
    for x, y, w, h, color, etiqueta in paisaje(nivel):
        caja(x, y, w, h, color)
    partes.append('</g>')
    y = parrafo(mision["objetivo"], 346, 18, 83, tema["acento"])+8
    y = parrafo(escena["texto"], y, 20, 73)+10
    caja(40, y-2, 820, 40, tema["panel"])
    texto(55, y+24, "✦ Examinar evidencia", 18)
    y = parrafo(escena["pista"], y+68, 17, 90)+10
    for opcion in escena["opciones"]:
        lineas = wrap(opcion["texto"], 80)
        alto = 18+len(lineas)*24
        caja(40, y, 820, alto, tema["panel"])
        for i, linea in enumerate(lineas):
            texto(55, y+26+i*24, linea, 18)
        y += alto+10
    if retro:
        y += 15
        y = parrafo("Defensa reforzada: +100 XP. Energía sin cambios.", y, 19, 75, tema["acento"])
        y = parrafo(escena["opciones"][0]["explicacion"], y+8, 17, 90)
        for i in range(12):
            caja(625+i*16, 150+(i%3)*5, 5, 5, ["#f5a623", "#d35274", "#398578"][i%3])
    else:
        y = parrafo("Elige cómo actuar. Cada decisión tiene consecuencias.", y+22, 17)
    caja(40, y+10, 820, 42, tema["panel"])
    texto(55, y+37, "Continuar" if retro else "Continuar · Disponible después de responder", 18)
    texto(40, y+83, "Reiniciar esta misión", 17)
    texto(40, y+113, "Mockup de diseño · No es una captura de ejecución", 13)
    alto = y+140
    fondo = [f'<rect width="1100" height="{alto+32}" fill="{tema["fondo"]}"/>']
    for x, y0, w, h, color, etiqueta in ambiente(nivel, 1100, alto+32):
        fondo.append(f'<rect x="{x}" y="{y0}" width="{w}" height="{h}" fill="{color}"/>')
    fondo.append(f'<svg x="100" y="16" width="900" height="{alto}" viewBox="0 0 900 {alto}">')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 {alto+32}" role="img" aria-label="{escape(mision["titulo"])} · Pantalla completa · {escape(tema["nombre"])}">'+''.join(fondo)+''.join(partes)+'</svg></svg>'
