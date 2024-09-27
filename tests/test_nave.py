import unittest
from app.nave import Nave
from app.acabado import Acabado
from app.vidrio import Vidrio


class TestNave(unittest.TestCase):
    def setUp(self):
        self.acabado = Acabado('pulido')
        self.vidrio_normal = Vidrio('transparente', esmerilado=False)
        self.vidrio_esmerilado = Vidrio('transparente', esmerilado=True)

    def test_calcular_area(self):
        nave = Nave(9, 15, False, self.acabado, self.vidrio_normal)
        self.assertEqual(nave.calcular_area(), 108)
        # Área = 9 * (15 - 3)

    def test_calcular_perimetro(self):
        nave = Nave(9, 15, False, self.acabado, self.vidrio_normal)
        self.assertEqual(nave.calcular_perimetro(), 30)
        # Perímetro = 2 * (9 + 6)

    def test_calcular_costo_nave_fija(self):
        nave = Nave(9, 15, False, self.acabado, self.vidrio_normal)
        costo = nave.calcular_costo('O')

    def test_calcular_costo_nave_movil(self):
        nave = Nave(9, 15, True, self.acabado, self.vidrio_esmerilado)
        costo = nave.calcular_costo('X')
        # Aquí deberías calcular el costo esperado y compararlo con el resultado
        # Ten en cuenta el costo adicional de la chapa y del vidrio esmerilado


if __name__ == '__main__':
    unittest.main()
