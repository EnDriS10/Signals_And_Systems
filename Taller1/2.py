
import math #para poder usar la constante
from math import* #para poder usar las funciones que usaremos

print("Programa multiusos")
a = input("Introduce un angulo en grados")
#para pasar de grados a radianes 
b = math.pi * float(a) / 180

print ("Su seno es ", sin(b), " y su coseno es ", cos(b))

c , d = input("Introduce el largo y el ancho de un rectangulo en ")
print("El área es ", c*d , "en cambio su perimetro es " , 2c + 2d)



#a = input("Escriba un numero")
#print(float(a) - 3)