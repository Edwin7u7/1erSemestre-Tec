# Pensamiento Computacional 2025 

Proyecto Final
Edwin Arturo Salgado Santana A00842140
Lenguaje a desarrollar el proyecto: Phyton

Este proyecto final surge a partir de una problemática en los restaurantes pequeños, locales de comida o incluso en las cafeterias de las escuelas, muchas veces debido al espacio muy reducido del puesto de comida, el contratar muchos empleados no es la mejor solución cuando hay un aumento exponencial de clientes que buscan ser atendidos de la forma mas rápida posible, por lo tanto este programa es donde entra, el cliente podrá interactuar con el programa con el fin de que podrá solicitar su orden en linea de una manera más rápida y eficiente cubriendo mas pedidos en menor tiempo posible y al final el ticket se imprimirá para ser pagado en caja y posteriormente recibir la orden.
Es interesante porque muchas veces el tiempo libre que una persona dispone para comer y posteriormente retomar sus actividades es muy corta y el esperar mucho tiempo en la fila le puede llegar a causar desesperación, es por eso que este problema cumple con el objetivo deseado y el cliente se va satisfecho.

Algoritmo:

Inicio:
  1 - Bienvenida al usuario
  
  2 - Se pide el nombre de la orden y fecha 
  
  3 - Mediante un while True se muestra al usuario el menú completo de comida/bebidas con un identificador único
  
  4 - Se pregunta al usuario que producto desea seleccionar
  
  5 - El usuario ingresa el identificador único del producto
  
  6 - Se muestran las especificaciones del producto (ingredientes, calorias, opción de ingredientes extras, precio)
  
  7 - Se pregunta al usuario si desea agregar el producto a la orden
    7.1 - Si la respuesta es "Si", se agrega el producto a una lista llamada "orden"
      7.1.1 - Se pregunta al usuario si desea terminar la orden 
        7.1.1.1 - Si la respuesta es "Si" sumar a PrecioFinal el precio del producto.
          7.1.1.1.1 - Romper el ciclo while True
          7.1.1.1.2 - Saltar al paso 8
        7.1.1.2 - Si la respuesta es "No", repetir el ciclo del paso 3.
    7.2 - Si la respuesta es "No"
      7.2.1 - Se pregunta al usuario si desea terminar la orden
        7.2.1.1 Si la respuesta es "Si", romper el ciclo while True, saltar al paso 8
        7.2.1.2 - Si la respuesta es "No", repetir el ciclo del paso 3.

  8 - if PrecioFinal == 0
    condicion  es true
    8.1 - Exit()
    condicion es false
    8.2 - Se muestra el ticket final al usuario con el precioFinal
      8.2.1 - Se pregunta al usuario el % de propina 
      8.2.2 - Se calcula el precioFinal con la propina aplicada

  9 - Se imprime el ticket final al usuario.
Fin del programa 
      
  

