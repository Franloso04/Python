'''fdatos= open("Carpeta.txt",encoding="utf_8")
for linea in fdatos:
    print(linea)
fdatos.close'''
'''fdatos=open("nombres.txt","w")
fdatos.write("Juan\nPepe\nJose")
fdatos.close'''

'''fdatos=open("nombres.txt","a")
fdatos.write("\nJuan\nPepe\nJose")
fdatos.close'''
try:
    fdatos= open("Carpeta.txt",encoding="utf_8")
except :
    fdatos=open("nombres.txt","w")
    fdatos.close()
    fdatos=open("nombres.txt","r")
    pass