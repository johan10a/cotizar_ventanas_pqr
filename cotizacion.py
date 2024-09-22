class Cotizacion:
    def __init__(self, ventanas, cantidad):
        self.ventanas = ventanas
        self.cantidad = cantidad
        self.total = self.calcular_total()
    
    def calcular_total(self):
        subtotal = sum(ventana.costo_total for ventana in self.ventanas)
        if self.cantidad > 100:
            subtotal *= 0.9  # Descuento del 10%
        return subtotal
