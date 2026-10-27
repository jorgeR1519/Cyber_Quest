import unittest

from logica_juego import Juego
from misiones import MISIONES


class PruebasJuego(unittest.TestCase):
    def test_nombre(self):
        for nombre in ("", "   ", "x" * 25):
            with self.assertRaises(ValueError):
                Juego(nombre)
        self.assertEqual(Juego(" Ada ").nombre, "Ada")

    def test_bloqueo_y_validaciones(self):
        juego = Juego("Ada")
        for nivel in (-1, 1, 4, True):
            with self.assertRaises(ValueError):
                juego.iniciar_mision(nivel)
        juego.iniciar_mision(0)
        with self.assertRaises(ValueError):
            juego.continuar()
        with self.assertRaises(ValueError):
            juego.decidir(2)
        juego.decidir(0)
        with self.assertRaises(ValueError):
            juego.decidir(0)
        self.assertEqual(juego.puntos, 100)

    def test_victoria_y_no_repeticion(self):
        juego = Juego("Ada")
        for i, mision in enumerate(MISIONES):
            juego.iniciar_mision(i)
            for _ in mision["escenas"]:
                juego.decidir(0)
                juego.continuar()
        self.assertTrue(juego.victoria)
        self.assertEqual(juego.puntos, 900)
        self.assertEqual(juego.energia, 3)
        with self.assertRaises(ValueError):
            juego.iniciar_mision(0)

    def test_derrota_y_limites(self):
        juego = Juego("Ada")
        juego.iniciar_mision(0)
        for _ in range(2):
            juego.decidir(1)
            juego.continuar()
        self.assertEqual(juego.energia, 2)  # Dos pérdidas y recuperación de una unidad.
        juego.iniciar_mision(1)
        juego.decidir(1)
        juego.continuar()
        juego.decidir(1)
        self.assertTrue(juego.derrota)
        self.assertEqual(juego.energia, 0)
        self.assertEqual(juego.puntos, 0)
        with self.assertRaises(ValueError):
            juego.continuar()
        with self.assertRaises(ValueError):
            juego.decidir(1)

    def test_reinicio_sin_acumular(self):
        juego = Juego("Ada")
        juego.iniciar_mision(0)
        juego.decidir(0)
        juego.continuar()
        juego.decidir(1)
        juego.reiniciar_mision()
        self.assertEqual((juego.puntos, juego.energia, juego.paso), (0, 3, 0))
        self.assertEqual(juego.historial, [])
        self.assertFalse(juego.pendiente)
        nuevo = Juego("Leo")
        self.assertEqual(nuevo.completadas, [])


if __name__ == "__main__":
    unittest.main()
