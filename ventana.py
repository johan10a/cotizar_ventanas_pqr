from nave import Nave

class Ventana:
    def __init__(self, estilo, ancho_total, alto_total, acabado, vidrio):
        self.estilo = estilo
        self.ancho_total = ancho_total
        self.alto_total = alto_total
        self.acabado = acabado
        self.vidrio = vidrio
        self.naves_fijas = []
        self.naves_moviles = []
        self.naves = self.crear_naves()  # Creamos las naves (fijas y móviles)
        self.costo_total = self.calcular_costo_total()

    def crear_naves(self):
        if self.estilo == 'O':
            # Estilo O: Solo una nave fija
            self.naves_fijas.append(Nave(self.ancho_total, self.alto_total, False, self.acabado, self.vidrio))
        
        elif self.estilo == 'XO':
            # Estilo XO: Una nave fija y una nave móvil
            ancho_nave = self.ancho_total / 2
            self.naves_fijas.append(Nave(ancho_nave, self.alto_total, False, self.acabado, self.vidrio))  # Fija
            self.naves_moviles.append(Nave(ancho_nave, self.alto_total, True, self.acabado, self.vidrio))   # Móvil
        
        elif self.estilo == 'OXO':
            # Estilo OXO: Dos naves fijas y una móvil
            ancho_nave = self.ancho_total / 3
            self.naves_fijas.append(Nave(ancho_nave, self.alto_total, False, self.acabado, self.vidrio))  # Fija
            self.naves_moviles.append(Nave(ancho_nave, self.alto_total, True, self.acabado, self.vidrio))   # Móvil
            self.naves_fijas.append(Nave(ancho_nave, self.alto_total, False, self.acabado, self.vidrio))  # Fija
        
        elif self.estilo == 'OXXO':
            # Estilo OXXO: Dos naves fijas y dos móviles
            ancho_nave = self.ancho_total / 4
            self.naves_fijas.append(Nave(ancho_nave, self.alto_total, False, self.acabado, self.vidrio))  # Fija
            self.naves_moviles.append(Nave(ancho_nave, self.alto_total, True, self.acabado, self.vidrio))   # Móvil
            self.naves_moviles.append(Nave(ancho_nave, self.alto_total, True, self.acabado, self.vidrio))   # Móvil
            self.naves_fijas.append(Nave(ancho_nave, self.alto_total, False, self.acabado, self.vidrio))  # Fija

        return self.naves_fijas + self.naves_moviles
    
    def calcular_costo_total(self):
        # Sumar el costo de las naves fijas y las naves móviles por separado
        costo_fijas = sum(nave.calcular_costo(self.estilo) for nave in self.naves_fijas)
        costo_moviles = sum(nave.calcular_costo(self.estilo) for nave in self.naves_moviles)
        
        print(f"Costo total naves fijas (O): {costo_fijas} COP")
        print(f"Costo total naves móviles (X): {costo_moviles} COP")
        
        # El costo total será la suma de ambos
        return costo_fijas + costo_moviles
