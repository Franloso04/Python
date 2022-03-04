#Mostrar menu agenda
def mostrarmenu():
    seleccion=0
    while(seleccion<1 or seleccion>6):
        print("1-Añadir Contacto")
        print("2-Borrar Contacto")
        print("3-Editar Contacto")
        print("4-Buscar Contacto")
        print("5-Mostrar Agenda")
        print("6-Salir")
        try:
            seleccion =int( input("Selecciona una opcion:"))
        except:
            seleccion=0
            print("Ten cuidado con lo que tecleas")
        if(seleccion<1 or seleccion>6):
            print("las opciones son hasta 6")
    return seleccion
#Añadir contacto a la agenda
def añadircontacto(vAgenda):
    print("************GUARDANDO CONTACTO************")
    nombre = input("Dime el nombre del contacto:")
    tel= input("Dime el número del contacto:")
    contacto = nombre+"-"+tel
    vAgenda.append(contacto)
#Mostrar todos los contactos
def mostrartodos(vAgenda):
    for contacto in vAgenda:
        print(contacto)
#Buscar contacto y devuelve su posicion 
def buscarcontacto(vAgenda):
    dato= input("Dime el nombre o el telefono a buscar")
    contador=0
    for i in vAgenda:

        if(i.find(dato) >= 0):
            return contador
        contador=contador+1
    print("Contacto no encontrado")
#Desglosar informacion de un contacto
def muestracontacto(vAgenda,index):
    if (index!= None):
        datos=vAgenda[index].split("-")
        print("Nombre:",datos[0])
        print("Telefono:",datos[1])
#Borrar Contacto
def borrarcontacto(vAgenda,index):
    if index!=None:
        
        vAgenda.pop(index)
#Editar Contacto
def editarcontacto(vAgenda,index):
    
    







print("************AGENDA DE CONTACTOS************")
vAgenda= []
opc=mostrarmenu()
while (opc != 6):
    if (opc==1):
        
        añadircontacto(vAgenda )
        
    elif(opc ==2):

        print("Opcion 2")
        borrarcontacto(vAgenda,buscarcontacto(vAgenda))
    elif(opc ==3):
        print("Opcion 3")
         
       
    elif(opc ==4):
        print("Opcion 4")
        muestracontacto(vAgenda,buscarcontacto(vAgenda))
        
    else:
        print("Tu agenda es:")
        mostrartodos(vAgenda)

    opc=mostrarmenu()
   
   
print("Saliendo de la agenda")
