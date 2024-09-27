from app.acabado import Acabado
from app.vidrio import Vidrio

class Nave:
    def __init__(self, ancho_cm, alto_cm, es_movil, acabado, vidrio):
        self.ancho_cm = ancho_cm
        self.alto_cm = alto_cm
        self.es_movil = es_movil
        self.acabado = acabado
        self.vidrio = vidrio
        self.costo_esquinas = 4310  # Costo por cada esquina
        self.costo_chapa = 16200    # Costo de la chapa en naves móviles

    def calcular_area(self):
        return self.ancho_cm * (self.alto_cm - 3)  # Reducimos solo el alto por 3 cm por el marco
    
    def calcular_perimetro(self):
        return 2 * (self.ancho_cm + 6)  # No reducimos nada aquí
    
    def calcular_costo(self, estilo):
        area = self.calcular_area()
        costo_vidrio = self.vidrio.calcular_costo(area)
        print(f"Área del vidrio: {area} cm², Costo del vidrio: {costo_vidrio} COP")
        
        perimetro = self.calcular_perimetro()
        costo_aluminio = self.acabado.precio_por_metro_lineal * (perimetro / 100)
        print(f"Perímetro del aluminio: {perimetro} cm, Costo del aluminio: {costo_aluminio} COP")
        
        # Calcular el costo de la chapa solo para naves móviles
        costo_chapa = 16200 if self.es_movil else 0
        print(f"Costo de la chapa: {costo_chapa} COP")
        
        # Calcular el costo de las esquinas
        costo_esquinas_total = 4 * self.costo_esquinas
        print(f"Costo de las esquinas: {costo_esquinas_total} COP")

        return costo_vidrio + costo_aluminio + costo_chapa + costo_esquinas_total
