#Edwin Arturo Salgado Santana A00842140

#Funciones
def aplicar_propina(precioTotal,propina):
    precio_con_propina = precioTotal + (precioTotal * (propina/100))
    return(precio_con_propina)
#Variables
precioTotal = 0
print('===========================')
#Aqui se inserta el nombre del restaurante o puesto de comida.
print ('//Nombre del restaurante//')

print('===========================')
#El usuario ingresa la fecha en que realizó su orden.
while True:
    try:
        dia = int(input("Ingresa el día:\n--> "))
        mes = int(input("Ingresa el mes:\n--> "))
        año = int(input("Ingresa el año:\n--> "))
        break
    except ValueError:
        print('ERROR.Ingresa un carácter válido.')

    

#Formato de fecha sujeto a cambios futuros.
fecha = (str(dia)+"/"+str(mes)+"/"+str(año))

print(fecha)
###########La impresión del menú y de la información en ella esta sujeto a cambios futuros, mediante la biblioteca
#de pandas y manejo de archivos .xlsx ##############
#Se definen las variables con los nombres de los alimentos y las bebidas.
comidaTipo1 = 'COMIDA 1'
comidaTipo2 = 'COMIDA 2'
comidaTipo3 = 'COMIDA 3'
bebidaTipo1 = 'BEBIDA 1'
bebidaTipo2 = 'BEBIDA 2'
bebidaTipo3 = 'BEBIDA 3'
#Se definen las variables con los precios de los alimentos y productos correspondientes.
precioComida1 = 100
precioComida2 = 135
precioComida3 = 225
precioBebida1= 50
precioBebida2 = 55
precioBebida3 = 70
extraIngredientes = 15


print('===================MENÚ=====================')
print('COMIDAS---------------------------BEBIDAS')
print('1.1-',comidaTipo1,'...$',precioComida1,'\t2.1-',bebidaTipo1,'...$',precioBebida1)
print('1.2-',comidaTipo2,'...$',precioComida2,'\t2.2-',bebidaTipo2,'...$',precioBebida2)
print('1.3-',comidaTipo3,'...$',precioComida3,'\t2.3-',bebidaTipo3,'...$',precioBebida3)
print('============================================')

while True:
    try:
        #Inicio de Orden
        print('------------------------------------------------')
        iniciarOrden = input('¿DESEA INICIAR LA ORDEN?(1-Si)-->')
        print('------------------------------------------------')
        if iniciarOrden == '1' or iniciarOrden == 'Si':
            #Se pide que el cliente agregue el nombre a que quiera asignar su orden.
            print('------------------------------------------------')
            nombreOrden = input('¿A QUE NOMBRE DESEA AGREGRAR LA ORDEN?\n -->')
            print('------------------------------------------------')
            #Mensaje de bienvenida.
            print('*********BIENVENIDO',nombreOrden.upper(),'*************')
            break
    except:
        print('ERROR.INTENTE DE NUEVO')
