import os
from createGrammar import globalGrammar
from press_enter import wait_for

def generateAP():
    
    grammarFinded = {}

    name = input("Introducir el nombre de la gramatica: ")
    for grammar in globalGrammar:
        if name == grammar.getName():
            grammarFinded = grammar
            break

    grammarFinded.setTransitions()

    print("Transiciones: ")
    for transition in grammarFinded.getTransitions():
        print(transition["string"])
    wait_for("", "\n")
    os.system('clear')