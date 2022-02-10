texto= input("Dime una palabra")
contador=0
letras=("a","e","i","o","u")
for x in letras:

    for i in texto:
        if i==x:
            print(x,end=" ")
            #continue 
            break
            
        
    
