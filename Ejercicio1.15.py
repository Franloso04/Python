
suma=0
c=0


n=int(input("Dime una serie de numeros acabada en -1 y te dire la media aritmetica"))
while n!=-1:
    suma= suma+n
    c= c+1
    n=int(input("Dime una serie de numeros acabada en -1 y te dire la media aritmetica"))


print ("La media de la serie de numeros es ",suma/c)