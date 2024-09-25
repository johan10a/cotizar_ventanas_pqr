class Acabado:
    precios = {
        'pulido': 50700,
        'lacado_brillante': 54200,
        'lacado_mate': 53600,
        'anodizado': 57300
    }
    
    def __init__(self, tipo):
        if tipo not in Acabado.precios:
            raise ValueError(f"Tipo de acabado '{tipo}' no válido")
        self.tipo = tipo
        self.precio_por_metro_lineal = Acabado.precios[tipo]
    
    def __str__(self):
        return f"Acabado {self.tipo}, Precio por cm lineal: {self.precio_por_metro_lineal}"
