from nave import Nave
class Ventana:
    def __init__(self, estilo, ancho_total, alto_total, acabado, vidrio):
        self.estilo = estilo
        self.ancho_total = ancho_total
        self.alto_total = alto_total
        self.acabado = acabado
        self.vidrio = vidrio
        self.naves = self.crear_naves()
        self.costo_total = self.calcular_costo_total()

    def crear_naves(self):
        naves = []
        if self.estilo == 'O':  # Ventana fija de un solo panel
            naves.append(Nave(self.ancho_total, self.alto_total, False, self.acabado, self.vidrio))
        return naves
    
    def calcular_costo_total(self):
        return sum(nave.calcular_costo() for nave in self.naves)
