# -*- coding: utf-8 -*-
"""
Created on Sun May  1 22:00:57 2022

@author: Diego Sanmiguel
"""

def traductor_de_frases_a_español(frase, diccionario):
    frase_list = frase.split()
    frase_list_traducida = []    

    for palabra in frase_list:        
        frase_list_traducida.append(diccionario[palabra])
        
    frase_en_español = " ".join(frase_list_traducida)
        
    return frase_en_español    
    

dictionary_example = {
	"gods": "dioses",
	"thank": "gracias",
	"I": "yo",
	"for": "por",
	"my": "mi",
	"soul": "alma",
    "am": "soy/estoy",
    "the": "el/la",
    "owner": "dueño",
    "of": "de",
    "destiny": "destino",
    "captain": "capitan",
    "love": "amor",
    "is": "es",
    "more": "más",
    "powerful": "poderoso",
    "than": "que",
    "fear": "miedo",
    "beautiful": "hermoso",
    "better": "mejor",
    "ugly": "feo",
    "Simple": "simple",
    "complex": "complejo",
    "complicated":"complicado"}

frase = input("ingrese frase: ")

frases = ["I thank gods for my soul", "I am the captain of my soul", 
          "love is more powerful than fear", "beautiful is better than ugly",
          "Simple is better than complex", "complex is better than complicated"]

for palabra in frase:
    if palabra not in dictionary_example:
        nueva_palabra = input("La palabra {} no existe por favor ingresa al diccionario: ".format(palabra))
        traduccion_nueva_palabra = input("Ingrese la tradcción de la palabra: ")
        dictionary_example[nueva_palabra] = traduccion_nueva_palabra

frases.append(frase)

for frase in frases:    
    print("las traducción de la frase --> {} es: ".format(frase) + "\n" + traductor_de_frases_a_español(frase, dictionary_example))
    print("-"*50)
    






