import sys
import os
from grammar_AP import menuGrammar
from valueFileGrammar import valueFileGrammar

def menu():
    while True:
        print("Menú General")
        print("1. Crear gramática")
        print("2. Cargar Archivo")
        print("3. Salir")
        opc = int(input("Escoje una opcion: "))
        os.system('clear')

        if opc == 1:
            menuGrammar()

        if opc == 2:
            route = input('Coloque una ruta:')
            routeArray = route.split('/')
            name = routeArray[-1].split(".")[0]
            files = open(route, 'r')
            print('Archivo cargado correctamente\n')
            valueFileGrammar(name, files)
            files.close()
    
        if opc == 3:
            break
