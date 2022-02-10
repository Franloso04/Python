nombre=input(print("Escribe una cadena de caracteres "))
palabra=input(print("Que palabra quieres buscar en tu cadena de caracteres"))
nombre.find(palabra)
print(nombre.find(palabra))
cont=0


while (nombre.find(palabra) != -1):
    cont += 1
    nombre = nombre[nombre.find(palabra)+1:]
print(cont)
    