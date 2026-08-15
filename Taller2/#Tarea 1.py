#Tarea 1

n = 1 #numero de veces de correr el texto
Cadena = input("introduce una frase")
Cadena2 = "" #cadena donde guardar el cifrado

for i in Cadena:
    a=chr(ord(i) + n) #recorre la cadena y va cambiando la letra
    Cadena2 = Cadena2 + a #almacena en la cadena

print(Cadena2)
