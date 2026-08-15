#Funciones


#Ejemplo

def factorial(n):
  fact = 1
  for x in range(1,n+1):
      fact = fact*x
  return fact

#return fact termina la funcion y opcionalmente retorna a quien lo llamo el valor de la expresion

fact = factorial(5)
print(fact)

#podemos volver a usar variable fact porque esta siendo usada dentro de la funcion que ya tuvo su return


#otros ejemplos

def doble(r):
  return 2*r

b=doble(3)
print(b)
print(doble(6))