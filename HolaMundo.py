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