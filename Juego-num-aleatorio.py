
import random 
aleatorio= (random.randint(0,10))
num= -1
bandera= True 
intentos=1

while num != aleatorio:
    
    num=(int(input("Dime un numero entre el 0 y el 10")))
    
    
       

    if (num < aleatorio):
        print("El aleatrio es mayor")
        intentos +=1
    elif (num > aleatorio):
        print("El aleatorio es menor")
        intentos +=1

print("Lo has adividado en", intentos, "intetos" )


