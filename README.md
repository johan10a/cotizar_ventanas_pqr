# Sistema de cotización de ventana empresa pqr

**Autor:** Johan Alexis Chara  
**Profesor:** Diego Fernando Marín  
**Curso:** Lenguaje de Programación Avanzado 1

## Descripción
El **Sistema de Cotización de Ventanas** es una aplicación diseñada para facilitar la cotización de ventanas personalizadas, considerando diferentes estilos, acabados y tipos de vidrio. Este sistema permite a los usuarios calcular el costo total de las ventanas en función de sus especificaciones, aplicando descuentos por volumen de pedido y proporcionando un desglose detallado de los costos involucrados.
## Funcionalidades Principales

- **Cotización de Ventanas**: Calcular el costo total de las ventanas basándose en el estilo (XO, O, OXO, OXXO), dimensiones, acabados y tipo de vidrio.
- **Gestión de Acabados**: Permitir al usuario seleccionar acabados específicos como pulido, lacado brillante, lacado mate y anodizado, cada uno con un costo asociado.
- **Opciones de Vidrio**: Ofrecer diferentes tipos de vidrio (transparente, bronce, azul) y la opción de vidrio esmerilado, con precios correspondientes.
- **Descuentos por Volumen**: Aplicar descuentos automáticamente si se piden más de 100 ventanas.
- **Cálculo Detallado de Costos**: Desglosar los costos en componentes como el costo del vidrio, el costo del aluminio, el costo de la chapa (para naves móviles) y el costo de las esquinas.

## Documentación 
El listado de requerimientos, y diagrama de clases (UML) se encuentran en la carpeta docs

### Descripción de Archivos y Clases

1. **main.py**: 
   - Contiene la función `main()` que orquesta la creación de acabados, vidrios, ventanas y cotizaciones. Es el punto de entrada para la ejecución del sistema.

2. **acabado.py**: 
   - Define la clase `Acabado`, que gestiona los diferentes tipos de acabados disponibles, sus precios y proporciona métodos para trabajar con estos.

3. **vidrio.py**: 
   - Define la clase `Vidrio`, que gestiona los diferentes tipos de vidrio, incluyendo precios y la opción de esmerilado.

4. **ventana.py**: 
   - Define la clase `Ventana`, que representa una ventana y calcula su costo total basándose en sus naves fijas y móviles.

5. **nave.py**: 
   - Define la clase `Nave`, que representa cada parte de la ventana (móvil o fija) y calcula su costo total en función de área, perímetro y acabados.

6. **cotizacion.py**: 
   - Define la clase `Cotizacion`, que calcula el costo total de un pedido de ventanas, aplicando descuentos si es necesario.

## Instrucciones de Uso
1. **Instalación**: Asegúrate de tener Python 3.12.5 instalado en tu máquina.
2. **Ejecución**: Ejecuta el archivo `main.py` desde la línea de comandos con la siguiente ruta:
   ```bash
   python cotizar_ventanas_pqr/cotizador/app/main.py

