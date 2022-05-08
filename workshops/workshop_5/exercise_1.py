# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:57:16 2022

@author: Diego Sanmiguel
"""

def consultar_por_tipo_plato(menu, tipo_plato):    
    for item_menu in menu:
        if tipo_plato == item_menu[1]:            
            print("-"*50)
            print(item_menu)
            print("-"*50)
            
def consultar_por_nombre_plato(menu, nombre_plato):    
    for item_menu in menu:
        if nombre_plato in item_menu[2]:            
            print("-"*50)
            print(item_menu)
            print("-"*50)        
           
def menu_por_tipo(menu):
    for item_menu in menu:
        menu_tipos_plato = {}
        items = []        
        if menu_tipos_plato.get(item_menu[1]):
            items.append(item_menu[2])
            menu_tipos_plato[item_menu[1]] = items
        else:
            items.append(item_menu[2])
            menu_tipos_plato[item_menu[1]] = items
            
    return menu_tipos_plato


def iniciar_aplicacion():
    
    menu = [
    ["ID004", "entrada", "ensalada"],
    ["ID008", "entrada", "sopa de tomate"],
    ["ID005", "entrada", "sopa de cebolla"],
    ["ID011", "bebida", "Jugo de Fresa"],
    ["ID012", "bebida", "Limonada Natural"],
    ["ID102", "plato fuerte", "pasta"],
    ["ID106", "plato fuerte", "lassagna"],
    ]
    
    ejecutando = True
    while ejecutando: 
        
        ejecutando = mostrar_menu_aplicacion(menu)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(menu) -> bool:
    
    print("Menu de opciones")
    print(" 1 - Consultar Menú")
    print(" 2 - Agregar nuevo elemento al menú")
    print(" 3 - Consultar opciones de menú por tipo de plato")
    print(" 4 - Consultar platos por nombre")
    print(" 5 - Listar el menú por tipo de plato")
    print(" 6 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        pass
    elif opcion_elegida == "2":
        pass
    elif opcion_elegida == "3":        
        tipo_plato = input("Digite el tipo de menú que desa consultar: ")
        consultar_por_tipo_plato(menu, tipo_plato)
    elif opcion_elegida == "4":
        nombre_plato = input("Digite el nombre del plato que desea consultar: ")
        consultar_por_nombre_plato(menu, nombre_plato)
    elif opcion_elegida == "5":
        pass
    elif opcion_elegida == "6":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando


iniciar_aplicacion()