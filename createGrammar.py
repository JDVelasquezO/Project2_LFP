from AP import AP
import os

def create_grammar():
    from menu import globalGrammars

    name = input("Escribir nombre de gramatica: ")
    ap = AP(name)
    globalGrammars.append(ap)

    while True:
        print("1. Ingresar Terminales")
        print("2. Ingresar NO Terminales")
        print("3. Ingresar Producciones")
        print("4. Borrar Producciones")
        print("5. No Terminal Inicial")
        print("6. Regresar")
        opc = int(input("Digita tu respuesta: "))
        os.system('clear')

        if opc == 1:
            T = input("Ingresar terminal: ")
            ap.setTerminals(T)
            os.system('clear')

        if opc == 2:
            nt = input("Ingresar no terminal: ")
            ap.setNonTerminals(nt)
            os.system('clear')

        if opc == 3:
            prod = input("Ingresar produccion: ")
            ap.setProductions(prod)
            os.system('clear')

        if opc == 4:
            prod = input("Ingresar produccion a borrar: ")
            ap.deleteProductions(prod)
            os.system('clear')

        if opc == 5:
            ntI = input("Ingresar No Terminal Inicial: ")
            ap.setNTInitial(ntI)
            os.system('clear')

        if opc == 6:
            break