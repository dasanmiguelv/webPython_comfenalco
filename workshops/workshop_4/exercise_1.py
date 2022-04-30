# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 09:25:05 2022

@author: Diego Sanmiguel
"""


numeros = [1, 3, 11, 12, 44, 8, 9, 10, 23, 9, 0, 213, 99, 98]

# a)	Hallar cuantos valores hay en la lista
print("-"*50)
cant_numeros = len(numeros)
print("La cantidad de números en la lista es de: ", cant_numeros)
print("-"*50)

# b)   Cuantos números son pares.
cant_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        cant_pares += 1
        
print("Hay {} número(s) pares en la lista".format(cant_pares))        
print("-"*50)


# c) Cuántos números son múltiplos de 3.
multiplos = []
cant_multiplos_de3 = 0
for numero in numeros:
    if numero != 0 and numero % 3 == 0:
        multiplos.append(numero)
        cant_multiplos_de3 += 1

print(multiplos)        
#print("Hay {} número(s) multiplos de 3 en la lista".format(cant_multiplos_de3))        
print("-"*50)

# d) Ordenar la lista de forma ascendente e imprimir el elemento en posición 5
numeros.sort()
print(numeros[5])

# Ordenar la lista de forma desencante e imprimir el elemento en posición 5
numeros.reverse()
print(numeros[5])


