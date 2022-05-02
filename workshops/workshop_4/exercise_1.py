# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 09:25:05 2022

@author: Diego Sanmiguel
"""


numeros = [1, 3, 11, 12, 44, 8, 9, 10, 23, 9, 0, 213, 99, 98]

# a)	Hallar cuantos valores hay en la lista
print("-"*50)
cant_numeros = len(numeros)
print("Punto a) \nLa cantidad de números en la lista es de: ", cant_numeros)
print("-"*50)

# b)   Cuantos números son pares.
cant_pares = 0
for numero in numeros:
    if numero != 0 and numero % 2 == 0:
        cant_pares += 1
        
print("Punto b) \nHay {} número(s) pares en la lista".format(cant_pares))        
print("-"*50)


# c) Cuántos números son múltiplos de 3.
multiplos_de3 = []
cant_multiplos_de3 = 0
for numero in numeros:
    if numero != 0 and numero % 3 == 0:
        multiplos_de3.append(numero)
        cant_multiplos_de3 += 1

#print("Hay {} número(s) multiplos de 3 en la lista".format(cant_multiplos_de3))        
print("Punto c) \nHay {} multiplo(s) de 3 en la lista".format(cant_multiplos_de3))
print("-"*50)

# d) Ordenar la lista de forma ascendente e imprimir el elemento en posición 5
numeros.sort()
print("Punto d) \nEl número ubicado en indicie 5 con la lista ordenada ascendentemente, es el: {}".format(numeros[5]))
print("-"*50)

# e) Ordenar la lista de forma desencante e imprimir el elemento en posición 5
numeros.reverse()
print("Punto e) \nEl número ubicado en indicie 5 con la lista ordenada descendentemente, es el: {}".format(numeros[5]))
print("-"*50)


# f) 	Hacer una sublista de elementos que se encuentren en el rango de 3, 50
sublista = []
for numero in numeros:
    if numero >= 3 and numero <= 50:
        sublista.append(numero)
        
sublista.sort()
print("Punto f) \nLa sublista de número(s) entre 3 y 50, es: {}".format(sublista))
print("-"*50)


# Reto Hacer una sublista de elementos de esta lista que sean números primos

def numeros_primos(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False    
        
    return True
            
sublista_numeros_primos = []
for numero in numeros:
    if numero == 0 or numero == 1:
        continue
    elif numero == 2:
        sublista_numeros_primos.append(2)
    else:
        validar_primo = numeros_primos(numero)        
        if validar_primo == True:
            sublista_numeros_primos.append(numero)    

print("Punto Reto \nLa sublista de número(s) primo(s), es: {}".format(sublista_numeros_primos))                
print("-"*50)