texto= input("Dime una palabra")
contador=0

for x in texto:
    if x==("a")or x==("e")or x==("i")or x==("o")or x==("u") : 
        contador+=1
    
print(contador)