"""Verifica la prioridad del audio sin reproducirlo en los altavoces."""
import unittest
from unittest.mock import Mock, patch

from sonidos import Sonidos


class PruebasSonidos(unittest.TestCase):
    def test_fondo_efecto_reanudacion_y_silencio(self):
        reloj = Mock()
        reloj.after.return_value = "temporizador"
        with patch("sonidos.winsound") as audio:
            audio.SND_FILENAME = 1
            audio.SND_ASYNC = 2
            audio.SND_LOOP = 4
            audio.SND_NODEFAULT = 8
            sonidos = Sonidos(reloj)
            try:
                sonidos.iniciar_fondo()
                self.assertEqual(audio.PlaySound.call_args.args, (sonidos.archivos["fondo"], 15))
                sonidos.tocar("acierto")
                self.assertEqual(audio.PlaySound.call_args.args, (sonidos.archivos["acierto"], 11))
                # El tiempo se programa según la duración del efecto, sin bloquear Tkinter.
                self.assertGreaterEqual(reloj.after.call_args.args[0], 320)
                sonidos.tocar("error")
                reloj.after_cancel.assert_called_with("temporizador")
                reloj.after.call_args.args[1]()
                self.assertEqual(audio.PlaySound.call_args.args, (sonidos.archivos["fondo"], 15))
                sonidos.tocar("victoria")
                sonidos.activo = False
                self.assertIsNone(sonidos.reanudacion)
                self.assertEqual(audio.PlaySound.call_args.args, (None, 0))
                llamadas = audio.PlaySound.call_count
                sonidos.tocar("acierto")
                self.assertEqual(audio.PlaySound.call_count, llamadas)
                sonidos.activo = True
                self.assertEqual(audio.PlaySound.call_args.args, (sonidos.archivos["fondo"], 15))
                sonidos.tocar("pista")
            finally:
                sonidos.cerrar()
            self.assertTrue(sonidos.cerrado)
            self.assertIsNone(sonidos.reanudacion)
