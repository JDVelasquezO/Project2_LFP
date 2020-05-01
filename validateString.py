from AP import AP
import os
from press_enter import wait_for

def validateString():
    from menu import globalGrammars
    grammarFinded = {}

    name = input("Introducir el nombre de la gramatica: ")
    for grammar in globalGrammars:
        if name == grammar.getName():
            grammarFinded = grammar
            break

    # for grammar in globalGrammarFiles:
    #     if name == grammar.getName():
    #         grammarFinded = grammar
    #         break

    # grammarFinded.setTransitions()
    string = input("Ingresa la cadena a evaluar: ")
    grammarFinded.generateAP(string)
    
    grammarFinded = {}
    # generateThree(grammarFinded, string)
    
    wait_for("", "\n")
    os.system('clear')