"""Actualiza módulos de compatibilidad y pruebas de la versión 2D."""
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[1]

ARCHIVOS = {
"interfaz.py": '"""Punto de importación de la interfaz de aventura Pygame."""\nfrom aventura import Aplicacion\n',
"logica_juego.py": '"""Punto de importación de las reglas de aventura."""\nfrom motor import Juego\n',
"misiones.py": '"""Punto de importación de los mapas y misiones de aventura."""\nfrom mundos import MISIONES\n',
"pruebas/test_logica.py": '''import math
import unittest
from collections import deque
import pygame
from motor import Juego
from mundos import MISIONES, ANCHO, ALTO


def ruta(juego, destino):
    inicio = (int((juego.x+10)//32),int((juego.y+12)//32))
    bloqueadas = set(juego.muros+juego.mision["peligros"])
    cola = deque([inicio]); prev = {inicio:None}
    while cola:
        p = cola.popleft()
        if p == destino:
            salida = []
            while p != inicio:
                salida.append(p); p = prev[p]
            return salida[::-1]
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            q = (p[0]+dx,p[1]+dy)
            if 0 <= q[0] < ANCHO and 0 <= q[1] < ALTO and q not in bloqueadas and q not in prev:
                prev[q] = p; cola.append(q)
    raise AssertionError(f"Destino inaccesible: nivel {juego.nivel+1}, {destino}")


def ir(juego, id):
    objeto = next(o for o in juego.objetos if o["id"] == id)
    for x,y in ruta(juego,(objeto["x"],objeto["y"])):
        tx,ty = x*32+6,y*32+4
        for _ in range(50):
            dx,dy = tx-juego.x,ty-juego.y
            if math.hypot(dx,dy) < 2.8:
                juego.x,juego.y = float(tx),float(ty); break
            juego.avanzar(1/60,dx,dy)
        else:
            raise AssertionError("Colisión inesperada en una ruta transitable")
    assert juego.cercano()["id"] == id, (id,juego.cercano())


def cerrar_dialogo(juego):
    while juego.dialogo:
        juego.interactuar()


class PruebasAventura(unittest.TestCase):
    def test_nombre_y_colisiones(self):
        for nombre in ("", "  ","x"*25):
            with self.assertRaises(ValueError): Juego(nombre)
        j = Juego(" Ada "); cerrar_dialogo(j)
        self.assertEqual(j.nombre,"Ada")
        for _ in range(300): j.avanzar(.016,-1,-1)
        self.assertFalse(j.solido(j.rect))
        self.assertGreaterEqual(j.x,32)

    def test_todos_los_objetos_son_alcanzables(self):
        j = Juego("Ada")
        for nivel in range(4):
            j.nivel = nivel; j.cargar_nivel(); cerrar_dialogo(j)
            for o in j.objetos:
                self.assertNotIn((o["x"],o["y"]),j.muros)
                self.assertNotIn((o["x"],o["y"]),j.mision["peligros"])
                ruta(j,(o["x"],o["y"]))

    def test_cuatro_misiones_mediante_movimiento_e_interaccion(self):
        j = Juego("Ada")
        for nivel in range(4):
            self.assertEqual(j.nivel,nivel)
            cerrar_dialogo(j); j.enemigos = []
            ir(j,"npc"); j.interactuar(); cerrar_dialogo(j)
            ir(j,"salida"); j.interactuar()
            self.assertEqual(j.nivel,nivel)  # El portal no acepta objetivos pendientes.
            if nivel == 0:
                for id,destino in (("correo","oficial"),("fraude1","cuarentena"),("fraude2","cuarentena")):
                    ir(j,id); j.escanear(); cerrar_dialogo(j); j.interactuar()
                    ir(j,destino); j.interactuar()
                    self.assertIn(id,j.hechos)
            else:
                orden = {1:["f1","f2","f3","sello","forja","factor"],
                         2:["e1","e2","e3","reporte"],
                         3:["c1","c2","c3","b1","b2","b3","h1","h2","h3"]}[nivel]
                for id in orden:
                    ir(j,id); j.interactuar()
                    self.assertIn(id,j.hechos)
            self.assertTrue(j.objetivo_completo())
            ir(j,"salida"); j.interactuar()
        self.assertTrue(j.victoria)
        self.assertEqual(j.completadas,[0,1,2,3])
        self.assertEqual(j.energia,5)

    def test_dano_invulnerabilidad_derrota_y_reinicio(self):
        j = Juego("Ada"); cerrar_dialogo(j)
        j.recibir_dano(); j.recibir_dano()
        self.assertEqual(j.energia,4)
        for _ in range(4):
            j.invulnerable = 0; j.recibir_dano()
        self.assertTrue(j.derrota)
        j.reiniciar_mision()
        self.assertFalse(j.derrota)
        self.assertEqual(j.energia,5)
        self.assertEqual(j.puntos,0)


if __name__ == "__main__": unittest.main()
''',
"pruebas/test_ayudas.py": '''import unittest
from motor import Juego
from test_logica import ir, cerrar_dialogo


class PruebasHerramientas(unittest.TestCase):
    def test_escaner_y_entrega_sin_preguntas(self):
        j = Juego("Ada"); cerrar_dialogo(j); j.enemigos = []
        ir(j,"npc"); j.interactuar(); cerrar_dialogo(j)
        ir(j,"correo"); j.interactuar()
        ir(j,"oficial"); j.interactuar()
        self.assertNotIn("correo",j.hechos)  # Hace falta inspeccionar, no adivinar.
        j.escanear(); cerrar_dialogo(j)
        self.assertIn("correo",j.inspeccionados)
        j.interactuar(); self.assertIn("correo",j.hechos)
        puntos = j.puntos; j.interactuar()
        self.assertEqual(j.puntos,puntos)

    def test_radio_limitada_y_reinicio(self):
        j = Juego("Ada"); cerrar_dialogo(j)
        for _ in range(4):
            j.consultar_radio(); cerrar_dialogo(j)
        self.assertEqual(j.radio,0)
        j.reiniciar_mision()
        self.assertEqual(j.radio,3)

    def test_mecanismos_rechazan_orden_incompleto(self):
        j = Juego("Ada")
        for nivel,id in ((1,"factor"),(2,"reporte"),(3,"h1"),(3,"b1")):
            j.nivel = nivel; j.cargar_nivel(); cerrar_dialogo(j); j.enemigos = []
            j.hechos.add("npc")
            ir(j,id); j.interactuar()
            self.assertNotIn(id,j.hechos)
            self.assertEqual(j.puntos,0)
''',
"pruebas/verificar_interfaz.py": '''"""Prueba del renderizado y eventos, sin ventana visible ni sonido."""
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
    app.nombre = "Prueba"; app.iniciar()
    for nivel in range(4):
        app.juego.nivel = nivel; app.juego.cargar_nivel()
        app.dibujar(); app.presentar()
        while app.juego.dialogo:
            app.manejar_evento(pg.event.Event(pg.KEYDOWN,key=pg.K_e,unicode="e"))
        app.actualizar(.016); app.dibujar()
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
''',
}


if __name__ == "__main__":
    for nombre,contenido in ARCHIVOS.items():
        (RAIZ/nombre).write_text(contenido,encoding="utf-8")
    print("Módulos y pruebas migrados a la aventura 2D.")
