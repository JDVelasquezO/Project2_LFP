from AP import AP
import os
from createGrammar import globalGrammar
from press_enter import wait_for
from generateThree import generateThree

def validateString():
    
    grammarFinded = {}

    name = input("Introducir el nombre de la gramatica: ")
    for grammar in globalGrammar:
        if name == grammar.getName():
            grammarFinded = grammar
            break

    # grammarFinded.setTransitions()
    string = input("Ingresa la cadena a evaluar: ")
    grammarFinded.generateAP(string)

    # generateThree(grammarFinded, string)
    
    wait_for("", "\n")
    os.system('clear')