from acabado import Acabado
from vidrio import Vidrio
from ventana import Ventana
from cotizacion import Cotizacion


def main():
    # Crear un acabado (pulido)
    acabado = Acabado('pulido')

    # Crear un vidrio transparente
    vidrio_esmerilado = Vidrio('transparente', esmerilado=False)# Si se desea colocar vidrio tipo esmerillado se cambia el False por True 


    # Crear una ventana de estilo XO
    ventana_xo = Ventana('XO', 18, 15, acabado, vidrio_esmerilado)     # Estilo XO

    # Crear una cotización para la ventana XO
    # ejemplo de descuento ventana el precio normal es 8.371.082 con descuento queda en 7.533.973
    cotizacion = Cotizacion([ventana_xo], 101)

    # Imprimir el costo total de la cotización
    print(f"El costo total de las ventanas es: {cotizacion.total} COP")


if __name__ == "__main__":
    main()
