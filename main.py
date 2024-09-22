from acabado import Acabado
from vidrio import Vidrio
from ventana import Ventana
from cotizacion import Cotizacion

def main():
    # Crear un acabado (pulido)
    acabado = Acabado('pulido')
    
    # Crear un vidrio transparente
    vidrio = Vidrio('transparente')
    
    # Aquí puedes cambiar el ancho y el alto de la ventana sin modificar la clase Nave
    ancho_cm = float(input("Ingrese el ancho de la ventana en cm: "))
    alto_cm = float(input("Ingrese el alto de la ventana en cm: "))
    
    # Crear una ventana estilo 'O' con las dimensiones ingresadas
    ventana = Ventana('O', ancho_cm, alto_cm, acabado, vidrio)
    
    # Crear una cotización para esta única ventana
    cotizacion = Cotizacion([ventana], 1)
    
    # Imprimir el costo total de la cotización
    print(f"El costo total es: {cotizacion.total} COP")

if __name__ == "__main__":
    main()
