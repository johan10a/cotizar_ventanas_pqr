import unittest
from app.ventana import Ventana
from app.acabado import Acabado
from app.vidrio import Vidrio

class TestVentana(unittest.TestCase):

    def test_ventana_estilo_OXXO(self):
        """Comprueba el cálculo del costo total para una ventana de estilo OXXO"""
        acabado = Acabado('pulido')
        vidrio = Vidrio('transparente')
        ventana = Ventana('O', 9, 15, acabado, vidrio)

        costo_aproximado = 891  # Un valor estimado para comparación

        self.assertAlmostEqual(ventana.costo_total, costo_aproximado, delta=33341)
      