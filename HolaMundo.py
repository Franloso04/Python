#Inicio de programa 
n=int(input("Dime tu edad y te dire tu edad dentro de 10 años"))

print("En diez años tendras",n+10)


if n>5:
    print("Es mayor que 5")
    print("Efectivamente")    
else:
    print("Es menor que 5")


while n==5:
    print("Repeticion")
    n+=1 #=que n= n+1

#Fin programa 
#try - except

try:
    num= int(input("Escribe un numero "))
    print(num+5)
except:
    print("El numero leido es una cadena de caracteres")


#import Numeros aleatorios 
import random 

print(random.randint(0,10))

#Numeros aleatorios 2 RANGE


import random
dias=["Lunes","Martes","Miercoles"]
dia=random.choice(dias)

print (dia)

lista = range(10)#=[0,1,2,3,4,5,6]

#Bucle for 
 for x in ["Lunes", "Martes", "Miercoles"]: # in range(1,12,2)Inicio, Fin, Con paso
     print(x)


#Listas 

vEdades=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18] #Definir un vector
vEdades[0]=20 #Dar valor a un espacio 
vEdades.append(19) #Inserccion
vEdades.sort() #
vEdades.pop()#Eliminar una posicion
vEdades.remove()#elimina un numero 
vEdades.
for edad in range(0,len(vEdades),2) :
    print (edad)



print (vEdades[0])

#Cadena de caracteres 
nombre="Fran     "
contador=0
nombre=nombre.strip()#Eliminar espacios
tam=len(nombre)#Tamaño

for i in nombre:#Recorrer cadena 
    print(i)
    if (i=="a"):
        contador+=1
print(contador )
nombre= nombre.lower()#pasar a minuscula
nombre= nombre.upper()#pasar a mayuscula


nombre.find("Fran")        
aux=nombre[nombre.find("Fran")+3: ]
print(nombre:4)#:para desde el principio hasta esa posicion o hasta el final 
aux.find("Fran")