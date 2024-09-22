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
        return 2* (self.ancho_cm + 6)  # No reducimos nada aquí
    
    def calcular_costo(self):
        area = self.calcular_area()
        costo_vidrio = self.vidrio.calcular_costo(area)
        print(f"Área del vidrio: {area} cm², Costo del vidrio: {costo_vidrio} COP")
        
        perimetro = self.calcular_perimetro()
        costo_aluminio = self.acabado.precio_por_metro_lineal * (perimetro / 100)
        print(f"Perímetro del aluminio: {perimetro} cm, Costo del aluminio: {costo_aluminio} COP")
        
        if self.es_movil:
            print(f"Costo de la chapa: {self.costo_chapa} COP")
            return costo_vidrio + costo_aluminio + self.costo_chapa
        else:
            costo_esquinas = 4 * self.costo_esquinas
            print(f"Costo de las esquinas: {costo_esquinas} COP")
            return costo_vidrio + costo_aluminio + costo_esquinas
