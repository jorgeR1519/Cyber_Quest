"""Paletas y escenarios pixel art compartidos entre Tkinter y los SVG."""
BASE = dict(nombre="Ciudad", fondo="#fff7eb", panel="#ffe4c4", texto="#493226",
            acento="#a64222", hover="#ffd29a", borde="#edc59c", cielo="#ffe7c5")
TEMAS = [
    dict(nombre="Cielo · Islas de nubes", fondo="#bde4ef", panel="#edf8fa", texto="#354854",
         acento="#934b27", hover="#ffdbab", borde="#b9d3df", cielo="#bde4ef"),
    dict(nombre="Selva · Sendero esmeralda", fondo="#80aa76", panel="#edf3d9", texto="#304634",
         acento="#765021", hover="#f3d996", borde="#adc494", cielo="#c7e1be"),
    dict(nombre="Cielo · Atardecer dorado", fondo="#e9aaa5", panel="#fff0e9", texto="#554051",
         acento="#964125", hover="#ffd59d", borde="#dcb5cc", cielo="#f2c1b7"),
    dict(nombre="Infierno · Fortaleza de lava", fondo="#86464c", panel="#ffe3c9", texto="#572e2b",
         acento="#9a321e", hover="#ffc183", borde="#dca086", cielo="#86464c"),
]


def ambiente(nivel, ancho, alto):
    """Decoración de pantalla completa; el centro se reserva para tarjetas legibles."""
    bloques = []
    def rect(x, y, w, h, color, etiqueta="ambiente"):
        bloques.append((x, y, w, h, color, etiqueta))
    if nivel in (0, 2):
        for y in range(35, int(alto), 170):
            for x in (12, ancho-95):
                rect(x+12, y, 48, 12, "#fff8ed", "nubes_fondo")
                rect(x, y+12, 78, 18, "#fff8ed", "nubes_fondo")
        rect(0, alto-20, ancho, 20, "#e8f6f7" if nivel == 0 else "#f9d8b6")
    elif nivel == 1:
        for x in (15, ancho-55):
            rect(x+14, 0, 20, alto, "#785c3d")
            for y in range(0, int(alto), 115):
                rect(x-15, y, 75, 35, "#356b48")
                rect(x-4, y+27, 56, 18, "#518753")
        for x in (80, ancho-83):
            rect(x, 0, 4, alto, "#4d7e43", "lianas_fondo")
        rect(0, alto-18, ancho, 18, "#597447")
    else:
        for y in range(20, int(alto), 140):
            for x in (12, ancho-74):
                rect(x, y, 60, 85, "#573d48")
                rect(x+10, y-12, 17, 20, "#573d48")
                rect(x+37, y-12, 17, 20, "#573d48")
                rect(x+25, y+20, 10, 30, "#ffb660", "brasas_fondo")
        rect(0, alto-28, ancho, 28, "#ed7c3e")
        for x in range(0, int(ancho), 65):
            rect(x, alto-17, 40, 6, "#ffd886", "brasas_fondo")
    return bloques


def paisaje(nivel=None):
    """Rectángulos (x, y, ancho, alto, color, etiqueta) en un lienzo 900×144."""
    tema = BASE if nivel is None else TEMAS[nivel]
    bloques = [(0, 0, 900, 144, tema["cielo"], "fondo")]
    def rect(x, y, w, h, color, etiqueta="paisaje"):
        bloques.append((x, y, w, h, color, etiqueta))
    def nube(x, y, color):
        rect(x+12, y, 48, 12, color, "nubes")
        rect(x, y+12, 84, 16, color, "nubes")
    if nivel in (0, 2):
        sol = "#ffda78" if nivel == 0 else "#ffb75e"
        rect(735, 14, 36, 48, sol); rect(729, 20, 48, 36, sol)
        for x, y in ((42, 18), (300, 12), (570, 35)):
            nube(x, y, "#fff9ee")
        for x in (50, 270, 510, 730):
            rect(x+12, 100, 120, 14, "#fffaf2")
            rect(x, 114, 150, 14, "#e7f3f0" if nivel == 0 else "#f9e4da")
            rect(x+24, 128, 96, 10, "#95bcc5" if nivel == 0 else "#c59ba8")
        # Torres flotantes: la misión conserva su contexto digital.
        for x, alto in ((360, 40), (405, 56), (450, 32)):
            rect(x, 100-alto, 30, alto, "#72a8bb" if nivel == 0 else "#ae7898")
            for y in range(100-alto+8, 95, 14):
                rect(x+8, y, 7, 6, "#fff0b5")
    elif nivel == 1:
        rect(0, 118, 900, 26, "#a7ba72")
        rect(0, 134, 900, 10, "#8c6649")
        for x in (20, 210, 450, 700, 840):
            rect(x+20, 45, 18, 78, "#986d46")
            for dx, y, w in ((0, 28, 58), (-12, 42, 82), (0, 57, 66)):
                rect(x+dx, y, w, 20, "#477b53")
            rect(x+10, 26, 30, 12, "#6b995b")
        for x in range(90, 900, 130):
            rect(x, 102, 42, 20, "#69985b")
            rect(x+12, 94, 20, 12, "#83ae64")
            rect(x+23, 112, 5, 5, "#f4bf64", "brillos")
        for x in (155, 590):
            rect(x, 14, 4, 60, "#70975d", "lianas")
    elif nivel == 3:
        rect(0, 116, 900, 28, "#e8753e")
        rect(0, 132, 900, 6, "#ffc16c", "lava")
        for x in range(0, 900, 95):
            rect(x, 105, 64, 18, "#5d4149")
            rect(x+12, 92, 40, 18, "#6f4950")
            rect(x+20, 138, 38, 4, "#ffe0a0", "lava")
        for x in (300, 360, 420, 480):
            rect(x, 42, 46, 65, "#533f49")
            rect(x-4, 32, 16, 16, "#533f49")
            rect(x+30, 32, 16, 16, "#533f49")
            rect(x+14, 62, 12, 20, "#ffb75e")
        for x, y in ((170, 70), (260, 27), (580, 52), (670, 15), (810, 62)):
            rect(x, y, 5, 5, "#ffd17c", "brasas")
    else:
        rect(0, 130, 900, 14, "#e3b77b")
        rect(0, 128, 900, 7, "#8aa66c")
        rect(60, 15, 36, 36, "#f3ac36")
        for x in (170, 430, 710):
            nube(x, 16, "#fffaf0")
        for columna in range(10):
            x, alto = 180+columna*64, 36+(columna % 4)*12
            rect(x, 128-alto, 44, alto, ("#e89b69", "#dfb563", "#d78d85", "#96b4a1")[columna % 4])
            for y in range(136-alto, 120, 18):
                rect(x+9, y, 8, 6, "#fff2bd")
    # El mismo guardián une visualmente todos los mundos.
    sprite = ["..cccc..", ".cccccc.", "..pppp..", "..ptpt..", "..pppp..",
              ".vvvvvv.", "pvovvovp", "..vvvv..", "..v..v..", ".tt..tt."]
    colores = dict(c="#b64839", p="#ffe1a3", t="#493226", v="#398578", o="#ffbf69")
    for fila, linea in enumerate(sprite):
        for columna, pixel in enumerate(linea):
            if pixel in colores:
                rect(90+columna*4, 70+fila*4, 4, 4, colores[pixel], "personaje")
    return bloques
