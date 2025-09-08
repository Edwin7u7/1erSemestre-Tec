#Edwin Arturo Salgado Santana A00842140
#Packages
import pandas as pd
#Funciones
def aplicar_propina(precioTotal,propina):
    precio_con_propina = precioTotal + (precioTotal * (propina/100))
    return(precio_con_propina)

def mostrarMenú(df):
    print(df)

def mostrarInfoProducto(id,df):
    df_product = df[df['Id'] == id]
    
    product = list(df_product['Producto'])
    if(product != []):
        print('----------------------------')
        print(list(product))
        print('----------------------------')
        print('Ingredientes:')
        ingredients = df_product['Ingredientes']
        print(list(ingredients))
        print('----------------------------')
        print('Precio:')
        precio = df_product['Precio']
        print(f'${list(precio)}')
        print('----------------------------')
        
        return precio
    else:
        precioMal = 0
        return (precioMal)

#Variables
df = pd.read_excel("Menú.xlsx")
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



'''print('===================MENÚ=====================')
print('COMIDAS---------------------------BEBIDAS')
print('1.1-',comidaTipo1,'...$',precioComida1,'\t2.1-',bebidaTipo1,'...$',precioBebida1)
print('1.2-',comidaTipo2,'...$',precioComida2,'\t2.2-',bebidaTipo2,'...$',precioBebida2)
print('1.3-',comidaTipo3,'...$',precioComida3,'\t2.3-',bebidaTipo3,'...$',precioBebida3)
print('============================================')'''
mostrarMenú(df)

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
        while iniciarOrden == '1' or iniciarOrden == 'Si':   
            while True:
                try:
                    print('------------------------------------------------')
                    prodSeleccionado = float(input('INGRESE EL ID DEL PRODUCTO-->'))
                    precio = mostrarInfoProducto(prodSeleccionado,df)
                    precio = int(precio)
                    if(precio != 0):
                        agregarProducto = input('DESEA AGREGAR EL PRODUCTO?(1:Si)--->')
                        if(agregarProducto == 'Si' or agregarProducto == '1'):
                            print('ProductoAgregado')
                            precio = int(precio)
                            precioTotal += precio
                            print(f'Precio hasta el momento ----> {precioTotal}')
                        else:
                           print('ERROR.SELECCIONE DE NUEVO.') 
                    else:
                       print('Producto Inexistente.') 
                except ValueError:
                    print('ERROR.Ingresa un carácter válido.')

            
    except:
        print('ERROR.INTENTE DE NUEVO')
