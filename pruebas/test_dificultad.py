import unittest
from motor import Juego
from dificultad import MODOS
from inteligencia import actualizar_centinela
from test_logica import cerrar_dialogo, ir


class PruebasDificultad(unittest.TestCase):
    def test_modos_validos_y_valores_iniciales(self):
        with self.assertRaises(ValueError): Juego("Ada","extremo")
        for modo,energia,radio in (("facil",7,5),("medio",5,3),("dificil",3,1)):
            j = Juego("Ada",modo)
            self.assertEqual((j.energia,j.ENERGIA_MAXIMA,j.radio),(energia,energia,radio))
            cerrar_dialogo(j); j.esquivar()
            self.assertEqual(j.espera_impulso,MODOS[modo]["impulso"])
            j.invulnerable = 0; j.recibir_dano()
            self.assertEqual(j.invulnerable,MODOS[modo]["proteccion"])
            j.reiniciar_mision()
            self.assertEqual((j.energia,j.radio,j.dificultad),(energia,radio,modo))

    def test_recuperacion_y_persistencia_entre_distritos(self):
        for modo,recuperacion in (("facil",2),("medio",1),("dificil",0)):
            j = Juego("Ada",modo); cerrar_dialogo(j); j.enemigos = []
            j.hechos.update(("npc","correo","fraude1","fraude2"))
            j.energia = 1; j.radio = 0
            ir(j,"salida"); j.interactuar()
            self.assertEqual(j.nivel,1)
            self.assertEqual(j.energia,1+recuperacion)
            self.assertEqual(j.radio,0)
            self.assertEqual(j.dificultad,modo)

    def test_fruta_y_limite_de_energia_en_cada_modo(self):
        for modo in MODOS:
            j = Juego("Ada",modo); cerrar_dialogo(j); j.enemigos = []
            ir(j,"fruta"); j.interactuar()
            self.assertNotIn("fruta",j.hechos)
            j.energia -= 1; j.interactuar()
            self.assertEqual(j.energia,j.ENERGIA_MAXIMA)
            self.assertIn("fruta",j.hechos)

    def test_velocidad_y_advertencia_realmente_varian(self):
        velocidades = []; avisos = []
        for modo in MODOS:
            j = Juego("Ada",modo); cerrar_dialogo(j)
            j.x,j.y = 262.,164.
            e = dict(x=197.,y=197.,inicio=197.,fin=325.,direccion=1)
            actualizar_centinela(j,e,.05)
            avisos.append(e["aviso"])
            e["estado"] = "persigue"
            actualizar_centinela(j,e,.05)
            velocidades.append(e["x"]-197.)
        self.assertLess(velocidades[0],velocidades[1])
        self.assertLess(velocidades[1],velocidades[2])
        self.assertGreater(avisos[0],avisos[1])
        self.assertGreater(avisos[1],avisos[2])
