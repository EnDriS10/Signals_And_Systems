#1

#metodos de complejos
a=complex(2,3) #complejo(Re,Im)
b= a.conjugate() #conjuga el complejo

#metodos de float
(-2.0).is_integer() #True
(3.2).is_integer() #False

#tenemos para metodos en cadenas

#x in s (true si cadena x esta en cadena s)
#x not in (true si la cadena x no esta en cadena s)
# x + s (concatenar las cadenas)

#Otros metodos de cadenas
cadena1 ="El hombre se hizo siempre, de todo material"

print(cadena1[0:(cadena1.find("e")+1)]) #imprimir desde el inicial hasta que encuentre la letra e
print()

#aumentar lista
lists = [[]] * 3
#lists output [[], [], []]
lists[0].append(3)
#lists output [[3], [3], [3]]
print(lists,"\n")

lists2 = [[] for i in range(3)] # si cambiamos el rango, al agregarle con append nos tira un error
lists2[0].append(3)
lists2[1].append(5)
lists2[2].append(7)
#lists2 output [[3], [5], [7]]
print(lists2,"\n")


# iterating through greet string
greet = 'Hello'
for letter in greet:
    print(letter)


cadena2 = "puto quien lea"
print(cadena2.replace("puto","mamawebazo"))
