import unittest
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
