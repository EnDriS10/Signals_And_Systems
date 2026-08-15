#Bucles y Condicionales

#range(star,end) empiza en star (inclusive) y termina en end (exclusive)
#range empieza por 0, y tiene otro apartado range(star,end,step)

#a = input("introduce un numero ")
#b= int(a)
#for i in range(1 , b):
#    b=b*i
#print(b)

#for x in range(1, 6):
#  print("El valor de x es ", x)
#  print("Su cuadrado es ", x ** 2)

for i in range(0, 6, 2):
    print(i)
print("FIN 1!")

#step va de 2 en 2

for x in range(5, 0, -1):
    print(x)
print("FIN 2!")

#esta vez va restando, aqui si no especifico el step no me daria como outpt el x

sum = 0
for i_2 in range(1, 11):
  sum = sum + (i_2 * i_2)
print("la suma de los primeros 10 cuadrados es", sum)
print("FIN 3!")