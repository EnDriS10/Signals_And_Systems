#Tarea

#Tarea 1

a= 5
for i in range(a+1):
    print("a "*i) #esto comenzara el bulce hasta que el numero de "a" sea igual a la variable
for i in range(a, 0, -1):
    i = i - 1
    print("a "*i) #completara la otra parte restando 


#Tarea 2

def Sumatoria(n):
    x=0 #se valora en 0 porque la funcion sumatoria si no suma vale 0
    for i in range(n): 
        x=x + i*(i+1) # recursividad
    return x

# Se provee al estudiante con un programa de prueba para verificar el correcto funcionamiento de la función anterior.
res_1 = Sumatoria(1)
res_2 = Sumatoria(2)
res_3 = Sumatoria(3)
res_5 = Sumatoria(5)

if res_1 == 0 and res_2 == 2 and res_3 == 8 and res_5 == 40:
  print("El funcionamiento es correcto")
else:
  print("El funcionamiento NO es correcto")