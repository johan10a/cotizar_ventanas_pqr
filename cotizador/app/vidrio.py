class Vidrio:
    precios = {
        'transparente': 8.25,
        'bronce': 9.15,
        'azul': 12.75
    }
    
    def __init__(self, tipo, esmerilado=False):
        if tipo not in Vidrio.precios:
            raise ValueError(f"Tipo de vidrio '{tipo}' no válido")
        self.tipo = tipo
        self.precio_por_cm2 = Vidrio.precios[tipo]
        self.esmerilado = esmerilado
        self.precio_esmerilado = 5.20 if esmerilado else 0 #Vidrio esmerillado
    
    def calcular_costo(self, area_cm2):
        return (self.precio_por_cm2 + self.precio_esmerilado) * area_cm2
    
    def __str__(self):
        return f"Vidrio {self.tipo}, Precio por cm²: {self.precio_por_cm2}, Esmerilado: {self.esmerilado}"
