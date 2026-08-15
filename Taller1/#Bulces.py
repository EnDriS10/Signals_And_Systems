#Bulces

x = 5
while x > 0:
    x -= 1
    print(x)
print('¡Fin 1!')

# todas las posibles variaciones de dos numeros

a = 0
b = 0
while a <= 3:
    while b <= 3:
        print(a,b) #iteraciones 
        b += 1  #accion del segundo while
    a += 1 #accion del primer while
    b = 0 # Reinicia b en cada iteración de a, al tabulado de a


# ejemplo del break para parar un ciclo
for x in range(5):
    if x == 3:
        break
print (x)
print ("Fin 3")

while True:
    respuesta = input('> ')
    if respuesta == 'salir':
        break
else:
    print(respuesta)
print ('¡Adiós!')
