n=int(input("Primera variable"))
m=int(input("Segunda variable"))
e=int(input("Tercera variable"))

if n>m and n>e:
    print(n, "Es el mayor de los tres")
if m>n and m>e:
    print(m, "Es el mayor de los tres")
if e>m and e>n:
    print(e, "Es el mayor de los tres")