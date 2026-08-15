#Numeros primos

from math import* #para importar ceil() que redondea hacia arriba

a = input("Introduzca un numero ")
b = ceil( int(a) / 2) +1
h = 2 #contador

for i in range(2 , b ):
    if (int(a)%i==0):
        h+=1

if(h!=2):
    print("El numero ",int(a)," tiene ", h, " divisores")
else:
    print("El numero ",int(a),"es primo")