

def imprimeconmayusculas(texto):
    
    
    texto= texto.lower()
    bandera=True
    for i in texto:
        if bandera:
            print(i.upper(),end="")
        else:
            print(i,end="")
        bandera= not(bandera)

texto= input("Dime una palabra")
imprimeconmayusculas(texto)
