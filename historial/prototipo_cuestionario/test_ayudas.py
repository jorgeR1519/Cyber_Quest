import unittest
from logica_juego import Juego
from misiones import MISIONES


class PruebasAyudas(unittest.TestCase):
    def test_descarte_preserva_respuesta_y_rechaza_opciones_eliminadas(self):
        juego = Juego("Ada")
        juego.iniciar_mision(0)
        juego.usar_ayuda("descarte")
        self.assertEqual(len(juego.descartadas), 2)
        self.assertNotIn(0, juego.descartadas)
        self.assertEqual(juego.ayudas["descarte"], 1)
        with self.assertRaises(ValueError):
            juego.decidir(juego.descartadas[0])
        juego.decidir(0)
        self.assertEqual(juego.puntos, 75)
        self.assertEqual(juego.energia, 3)
        with self.assertRaises(ValueError):
            juego.usar_ayuda("pista")

    def test_costes_combinados_y_sin_repeticion(self):
        juego = Juego("Ada")
        juego.iniciar_mision(0)
        for ayuda in ("pista", "descarte", "mentor"):
            self.assertTrue(juego.usar_ayuda(ayuda))
        with self.assertRaises(ValueError):
            juego.usar_ayuda("pista")
        self.assertEqual(juego.recompensa, 20)
        resultado = juego.decidir(0)
        self.assertEqual(resultado["premio"], 20)
        juego.continuar()
        self.assertEqual(juego.recompensa, 100)
        self.assertEqual(juego.descartadas, [])
        with self.assertRaises(ValueError):
            juego.usar_ayuda("mentor")

    def test_reinicio_restaura_recursos_y_evitar_acumulacion(self):
        juego = Juego("Ada")
        juego.iniciar_mision(0)
        juego.usar_ayuda("mentor")
        juego.decidir(0)
        juego.reiniciar_mision()
        self.assertEqual(juego.ayudas, {"pista": 3, "descarte": 2, "mentor": 1})
        self.assertEqual(juego.historial, [])
        self.assertEqual(juego.puntos, 0)
        self.assertEqual(juego.recompensa, 100)

    def test_disponibilidad_global_y_datos_de_las_misiones(self):
        juego = Juego("Ada")
        with self.assertRaises(ValueError):
            juego.usar_ayuda("pista")
        for nivel, mision in enumerate(MISIONES):
            juego.iniciar_mision(nivel)
            for escena in mision["escenas"]:
                self.assertEqual(len(escena["opciones"]), 4)
                self.assertEqual(sum(op["segura"] for op in escena["opciones"]), 1)
                if juego.ayudas["pista"]:
                    juego.usar_ayuda("pista")
                juego.decidir(0)
                juego.continuar()
        self.assertTrue(juego.victoria)
        self.assertEqual(juego.ayudas["pista"], 0)
        self.assertEqual(juego.puntos, 855)
