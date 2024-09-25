from acabado import Acabado
from vidrio import Vidrio
from ventana import Ventana
from cotizacion import Cotizacion

def main():
    # Crear un acabado (pulido)
    acabado = Acabado('pulido')
    
    # Crear un vidrio transparente
    vidrio = Vidrio('transparente')
    
    # Crear una ventana de estilo XO
    ventana_xo = Ventana('XO', 18, 15, acabado, vidrio)     # Estilo XO
    
    # Crear una cotización para la ventana XO
    cotizacion = Cotizacion([ventana_xo], 101)#ejemplo de descuento ventana
    
    # Imprimir el costo total de la cotización
    print(f"El costo total de las ventanas es: {cotizacion.total} COP")

if __name__ == "__main__":
    main()
