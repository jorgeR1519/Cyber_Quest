import math
import unittest
import pygame
from motor import Juego
from inteligencia import actualizar_centinela


class PruebasCentinelas(unittest.TestCase):
    def preparar(self):
        j = Juego("Ada"); j.dialogo = []; j.x,j.y = 262.,164.
        e = dict(x=197.,y=197.,inicio=197.,fin=325.,direccion=1)
        return j,e

    def test_detecta_avisa_y_persigue_en_dos_ejes(self):
        j,e = self.preparar()
        actualizar_centinela(j,e,.05)
        self.assertEqual(e["estado"],"alerta")
        self.assertEqual((e["x"],e["y"]),(197.,197.))
        for _ in range(60): actualizar_centinela(j,e,.05)
        self.assertEqual(e["estado"],"persigue")
        self.assertLess(e["y"],190)
        self.assertGreater(e["x"],220)

    def test_pared_bloquea_vision_y_refugio_protege(self):
        j,e = self.preparar()
        j.muros.append((7,6))
        actualizar_centinela(j,e,.05)
        self.assertNotIn(e["estado"],("alerta","persigue"))
        j.x,j.y = 70.,68.; e["x"],e["y"] = 160.,68.
        for _ in range(60): actualizar_centinela(j,e,.05)
        self.assertNotEqual(e["estado"],"persigue")
        self.assertFalse(pygame.Rect(e["x"],e["y"],23,23).colliderect(pygame.Rect(32,32,128,96)))

    def test_busca_ultima_posicion_y_regresa_sin_cruzar_paredes(self):
        j,e = self.preparar()
        for _ in range(20): actualizar_centinela(j,e,.05)
        j.x,j.y = 710.,420.
        for _ in range(180):
            actualizar_centinela(j,e,.05)
            self.assertFalse(j.solido(pygame.Rect(e["x"],e["y"],23,23)))
        self.assertIn(e["estado"],("patrulla","regreso"))

    def test_lava_persigue_mas_rapido_y_dialogos_congelan_amenazas(self):
        distancias = []
        for nivel in (0,3):
            j,e = self.preparar(); j.nivel = nivel
            e.update(estado="persigue",memoria=2.,visto=(j.x,j.y))
            actualizar_centinela(j,e,.05)
            distancias.append(math.dist((197,197),(e["x"],e["y"])))
        self.assertGreater(distancias[1],distancias[0])
        j.enemigos = [e]; j.dialogo = ["Lee con calma"]
        antes = e["x"],e["y"]
        j.avanzar(.05)
        self.assertEqual(antes,(e["x"],e["y"]))

    def test_persigue_rodeando_un_obstaculo(self):
        j,e = self.preparar()
        j.x,j.y = 293.,197.
        j.muros.append((7,6))
        e.update(estado="persigue",memoria=3.,visto=(j.x,j.y))
        for _ in range(60):
            actualizar_centinela(j,e,.05)
            self.assertFalse(j.solido(pygame.Rect(e["x"],e["y"],23,23)))
        self.assertLess(math.dist((e["x"],e["y"]),(j.x,j.y)),20)


class PruebasGuia(unittest.TestCase):
    def test_paso_a_paso_y_ruta_transitable(self):
        j = Juego("Ada")
        self.assertEqual(j.guia_actual()[0]["id"],"npc")
        j.hechos.add("npc")
        objetivo,texto = j.guia_actual()
        self.assertEqual(objetivo["tipo"],"mensaje")
        self.assertTrue(j.ruta_guia())
        self.assertTrue(all(p not in j.muros+j.mision["peligros"] for p in j.ruta_guia()))
        j.carga = "correo"
        self.assertIsNone(j.guia_actual()[0])
        self.assertIn("F",j.guia_actual()[1])
        j.inspeccionados.add("correo")
        self.assertEqual(j.guia_actual()[0]["id"],"oficial")
        j.hechos.update(("correo","fraude1","fraude2")); j.carga = None
        self.assertEqual(j.guia_actual()[0]["id"],"salida")

    def test_tutorial_gratuito_no_gasta_radio(self):
        j = Juego("Ada"); j.dialogo = []
        j.ver_tutorial()
        self.assertTrue(j.dialogo)
        self.assertEqual(j.radio,3)
