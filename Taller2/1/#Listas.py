
#Listas en Python
#Las listas son colecciones ordenadas y modificables de elementos. Aprenderemos cómo agregar, modificar y eliminar elementos de una lista.

#Agregar elementos a una lista:
#list[num]=valor
frutas = ["manzana", "banana", "cereza"]
frutas.append(“naranja”) # Agregar un elemento al final de la lista

#Modificar elementos de una lista:
frutas[1] = "pera" # Modificar el segundo elemento de la lista
Eliminar elementos de una lista:

frutas.remove("manzana") # Eliminar un elemento específico
del frutas[0] # Eliminar el primer elemento de la lista



#Diccionarios en Python
#Dictionary[clave]=valor
#Los diccionarios son colecciones de pares clave-valor. Aprenderemos cómo agregar, modificar y eliminar elementos de un diccionario.

#Agregar elementos a un diccionario:
persona = {“nombre”: “Juan”, “edad”: 30}
persona[“ciudad”] = “Miami” # Agregar un par clave-valor al diccionario

#Modificar elementos de un diccionario:
persona[“edad”] = 31 # Modificar el valor de una clave existente

#Eliminar elementos de un diccionario:
del persona[“ciudad”] # Eliminar un par clave-valor específico
persona.pop(“edad”) # Eliminar un par clave-valor y obtener su valor



#Crear Strings en Python
#Los strings son secuencias de caracteres. Puedes crearlos utilizando comillas simples o dobles:

cadena1 = 'Hola, mundo!'
cadena2 = "Python es genial"

#Transformar Strings en Python

#Mayúsculas y minúsculas:
texto = "Python es genial"
mayusculas = texto.upper() # Convierte a mayúsculas
minusculas = texto.lower() # Convierte a minúsculas

#Concatenación de Strings:
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido # Concatenación de strings

#Separar Strings:

frase = "Hola, cómo estás?"
palabras = frase.split(", ") # Divide la cadena en una lista de palabras