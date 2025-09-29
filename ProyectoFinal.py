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
        procesoDia = True
        procesoMes = True
        procesoAño = True
        while procesoDia == True:
            print('------------------------------------------------')
            dia = int(input("Ingresa el día:\n--> "))
            print('------------------------------------------------')
            if( 0< dia < 31 ):
                procesoDia = False
            else:
                print('------------------------------------------------')
                print('Ingrese un día válido')
                print('------------------------------------------------')
        while procesoMes == True: 
            print('------------------------------------------------')   
            mes = int(input("Ingresa el mes:\n--> "))
            print('------------------------------------------------')
            if(0< mes <13):
                procesoMes = False
            else:
                print('------------------------------------------------')
                print('Ingrese un mes válido')
                print('------------------------------------------------')
        while procesoAño == True:
            print('------------------------------------------------')
            año = int(input("Ingresa el año:\n--> "))
            print('------------------------------------------------')
            if(año == 2025):
                procesoAño = False
            else:
                print('------------------------------------------------')
                print('Ingrese el año actual')
                print('------------------------------------------------')
        break
    except ValueError:
        print('ERROR.Ingresa un carácter válido.')

    

#Formato de fecha sujeto a cambios futuros.
fecha = (str(dia)+"/"+str(mes)+"/"+str(año))

print(fecha)




'''print('===================MENÚ=====================')
print('COMIDAS---------------------------BEBIDAS')
print('1.1-',comidaTipo1,'...$',precioComida1,'\t2.1-',bebidaTipo1,'...$',precioBebida1)
print('1.2-',comidaTipo2,'...$',precioComida2,'\t2.2-',bebidaTipo2,'...$',precioBebida2)
print('1.3-',comidaTipo3,'...$',precioComida3,'\t2.3-',bebidaTipo3,'...$',precioBebida3)
print('============================================')'''
print("*********************Menú**********************")
mostrarMenú(df)
#Inicio de Orden
try:
    print('------------------------------------------------')
    iniciarOrden = input('¿DESEA INICIAR LA ORDEN?(1-Si)-->')
    print('------------------------------------------------')
except:
    print('Error. Intente de nuevo')
    
    
if iniciarOrden == '1' or iniciarOrden == 'Si':
    #Se pide que el cliente agregue el nombre a que quiera asignar su orden.
    print('------------------------------------------------')
    nombreOrden = input('¿A QUE NOMBRE DESEA AGREGRAR LA ORDEN?\n -->')
    print('------------------------------------------------')
    #Mensaje de bienvenida.
    print('*********BIENVENIDO',nombreOrden.upper(),'*************')
    while iniciarOrden == '1' or iniciarOrden == 'Si':   
        try:
            print('------------------------------------------------')
            prodSeleccionado = float(input('INGRESE EL ID DEL PRODUCTO---> '))
            print('------------------------------------------------')
            precio = mostrarInfoProducto(prodSeleccionado,df)
            precio = int(precio)
            if(precio != 0):
                print('------------------------------------------------')
                agregarProducto = input('DESEA AGREGAR EL PRODUCTO?(1:Si)(2:No)--->')
                print('------------------------------------------------')
                if(agregarProducto == 'Si' or agregarProducto == '1'):
                    print('ProductoAgregado')
                    precio = int(precio)
                    precioTotal += precio
                    print('------------------------------------------------')
                    print(f'Precio hasta el momento ----> ${precioTotal}')
                    print('------------------------------------------------')
                    print('------------------------------------------------')
                    terminar = input('Desea terminar la orden?(1-Si)(2-No)')
                    print('------------------------------------------------')
                    if terminar in[ 'Si' , '1' ,'si']:
                        iniciarOrden = '2'
                        
                    elif terminar in ['No' , '2' , 'no'] :
                        iniciarOrden = '1'
                elif (agregarProducto == 'No' or agregarProducto == '2' or agregarProducto == 'no'):
                    print('------------------------------------------------')
                    terminar = input('Desea terminar la orden?(2-No)(1-Si)')
                    print('------------------------------------------------')
                    if terminar in[ 'Si' , '1' ,'si']:
                        iniciarOrden = '2'
                    elif terminar in ['No' , '2' , 'no']:
                        iniciarOrden = '1'
                else:
                    print('ERROR.SELECCIONE DE NUEVO.') 

                

            else:
                print('Producto Inexistente.') 
        except ValueError:
            print('ERROR.Ingresa un carácter válido.')
else:
    print('Orden terminada...')
    exit()
        
if(precioTotal > 0):
    while True:
        try:
            print('------------------------------------------------')
            propina = input('Ingresa el %porcentaje de propina: ')
            print('------------------------------------------------')
            propina = int(propina)
            
            if(propina >=0):
                precioTotal = aplicar_propina(precioTotal, propina)
                print('------------------------------------------------')
                print(f'El precio total es: ${precioTotal}')
                print('------------------------------------------------')
                break
            if(propina <0):
                print('Ingrese una propina válida. Intente de nuevo...')
            
        except ValueError:
            print('Ingrese un carácter correcto...')
    
else:
    print('Orden finalizada')
    exit()
print('Orden finalizada. Disfrute su compra...') 
exit()  
    
