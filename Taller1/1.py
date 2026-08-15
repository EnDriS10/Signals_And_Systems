# Ejecutar el siguiente código para observar el funcionamiento de la instrucción input.

dia = input("¿Qué día es hoy? (Escribir un número del 1 al 31)")
mes = input("¿En qué mes estamos? (Escribir un número del 1 al 12)")
print("Hoy es", dia, "del mes", mes)

# dia = input("orden") corresponde a introcuir un valor como string
# el comando int(dia) convierte el valor introducido (string) en (int) y permite operar 


print("Faltan",  (22 - int(dia)+(12-int(mes))*30), "días para las vacaciones de navidad")

# Las vacaciones de navidad empiezan el 22 de diciembre
