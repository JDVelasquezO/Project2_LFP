import sys
import os
from grammar_AP import menuGrammar

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

        if opc == 3:
            break
