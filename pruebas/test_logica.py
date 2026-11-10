import math
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
        self.assertEqual(j.puntos,2475)

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
