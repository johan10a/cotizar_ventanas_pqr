import unittest
from app.acabado import Acabado

class TestAcabado(unittest.TestCase):
    def test_precio_valido(self):
        acabado = Acabado('pulido')
        self.assertEqual(acabado.precio_por_metro_lineal, 50700)

    def test_precio_invalido(self):
        with self.assertRaises(ValueError):
            Acabado('invalido')

    def test_str_representation(self):
        acabado = Acabado('lacado_brillante')
        self.assertEqual(str(acabado), "Acabado lacado_brillante, Precio por cm lineal: 54200")