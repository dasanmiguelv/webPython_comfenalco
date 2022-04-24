# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:08:27 2022

@author: Diego Sanmiguel
"""

cancion_baby_shark = """Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!

Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!

Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!

Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!

Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!

Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt!

Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away!

Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last!

It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end!
"""
palabra_shark = "shark"
palabra_doo = "doo"

veces_shark = cancion_baby_shark.count(palabra_shark)
veces_doo = cancion_baby_shark.count(palabra_doo)

cantidad_palabras = len(cancion_baby_shark.split())

print("-"*50)
print("La cación 'baby shark' tiene '{}' palabras.".format(cantidad_palabras))
print("-"*50)
print("La palabra '{}' está '{}' veces en la cancion baby shark.\nLa palabra '{}' está '{}' veces en la cancion baby shark.".format(palabra_shark, veces_shark, palabra_doo, veces_doo))
print("-"*50)