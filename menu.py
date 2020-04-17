import sys
import os

def menu():    
    while True:
        print("Menú General")
        print("1. Crear AFD")
        print("2. Crear gramática")
        print("3. Evaluar cadenas")
        print("4. Cargar Archivo")
        print("5. Agregar gramática tipo 2 y AP")
        print("6. Reportes")
        print("7. Salir")
        opc = int(input("Escoje una opcion: "))
        os.system('clear')

        if opc == 6:
            break
