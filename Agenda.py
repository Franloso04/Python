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
    contacto = nombre+"---"+tel
    vAgenda.append(contacto)
#Mostrar todos los contactos
def mostrartodos(vAgenda):
    for contacto in vAgenda:
        print(contacto)
        

print("************AGENDA DE CONTACTOS************")
vAgenda= []
opc=mostrarmenu()
while (opc != 6):
    if (opc==1):
        añadircontacto(vAgenda )
        print("Opcion 1")
    elif(opc==2):
        print("Opcion 2")
    elif(opc==3):
        print("Opcion 3")
    elif(opc==4):
        print("Opcion 4")
    else:
        print("Tu agenda es:")
        mostrartodos()

    opc=mostrarmenu()
   
   
print("Saliendo de la agenda")
