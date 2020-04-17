import sys
import os
from createGrammar import create_grammar
from generateAP import generateAP

def menuGrammar():    
    while True:
        print("Menú General")
        print("1. Ingresar / Modificar gramática")
        print("2. Generar AP")
        print("3. Visualizar Automata")
        print("4. Validar Cadenas")
        print("5. Regresar")
        print("6. Salir")
        opc = int(input("Escoje una opcion: "))
        os.system('clear')

        if opc == 1:
            create_grammar()

        if opc == 2:
            generateAP()

        if opc == 6:
            break
