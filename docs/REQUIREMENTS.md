# Requerimientos para el Sistema de Cotización de Ventanas 

## Requerimientos Funcionales

1. **Estilos de ventana**:
   - El sistema debe soportar los estilos de ventana: O, XO, OXXO y OXO.
   - Se debe calcular el tamaño de cada nave basado en el estilo de la ventana y las dimensiones totales.

2. **Materiales**:
   - Se debe tener en cuenta un solo tipo de aluminio con los siguientes acabados:
     - Pulido
     - Lacado Brillante
     - Lacado Mate
     - Anodizado
   - El costo del aluminio debe calcularse por cm lineal del marco de cada nave, restando las esquinas y considerando que los perfiles de aluminio se insertan en las esquinas.

3. **Tipos de vidrio**:
   - El sistema debe permitir seleccionar entre tres tipos de vidrio:
     - Transparente
     - Bronce
     - Azul
   - El costo del vidrio se calcula por cm² (área) y debe ser 1.5 cm más pequeño en cada lado del tamaño de la nave.

4. **Esquinas y chapas**:
   - El sistema debe incluir el costo de las esquinas y las chapas.
   - Cada esquina tiene un costo específico de $4,310.
   - Cada nave móvil (X) debe incluir el costo de una chapa de $16,200.

5. **Cálculos**:
   - El sistema debe calcular el costo total de una ventana considerando:
     - Aluminio (acabado)
     - Vidrio 
     - Chapas (si aplica)
     - Esquinas
   - El costo del aluminio debe incluir los perfiles, restando el tamaño de las esquinas y considerando su inserción.
   - El costo del vidrio debe calcularse por el área visible (ancho x alto de la nave menos 1.5 cm en cada lado).

6. **Descuentos**:
   - El sistema debe aplicar un descuento del 10% cuando la cantidad de ventanas solicitadas supere las 100 unidades.

## Requerimientos No Funcionales



1. **Interfaz de usuario**:
   - El sistema debe ser fácil de usar, permitiendo a los usuarios ingresar las dimensiones, seleccionar el estilo de ventana y los materiales, y generar una cotización de manera rápida y eficiente.

2. **Reporte y cotización**:
   - El sistema debe generar un reporte detallado con el costo desglosado por cada material y nave.