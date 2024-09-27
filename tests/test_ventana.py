import unittest
from app.nave import Nave
from app.acabado import Acabado
from app.vidrio import Vidrio
from app.ventana import Ventana  

class TestVentana(unittest.TestCase):

    def setUp(self):
        self.acabado = Acabado('pulido')
        self.vidrio = Vidrio('transparente', esmerilado=False)

    def test_crear_nave_fija_estilo_O(self):
        ventana = Ventana('O', 9, 15, self.acabado, self.vidrio)
        self.assertEqual(len(ventana.naves_fijas), 1)
        self.assertEqual(len(ventana.naves_moviles), 0)
        print(" ")

    def test_calcular_costo_ventana_O(self):
        ventana = Ventana('O', 9, 15, self.acabado, self.vidrio)
        costo_total = ventana.calcular_costo_total()
        self.assertEqual(costo_total, 33341)  
        print(" ")

    def test_calcular_costo_ventana_XO(self):
        ventana = Ventana('XO', 18, 15, self.acabado, self.vidrio)
        costo_total = ventana.calcular_costo_total()
        self.assertEqual(costo_total, 82882)  
        print(" ")

    def test_calcular_costo_ventana_OXO(self):
        ventana = Ventana('OXO', 27, 15, self.acabado, self.vidrio)
        costo_total = ventana.calcular_costo_total()
        self.assertEqual(costo_total, 116223)  
        print(" ")

    def test_calcular_costo_ventana_OXXO(self):
        ventana = Ventana('OXXO', 36, 15, self.acabado, self.vidrio)
        costo_total = ventana.calcular_costo_total()
        self.assertEqual(costo_total, 165764) 
        print(" ")

if __name__ == '__main__':
    unittest.main()
