import os
from press_enter import wait_for

def generateAP():
    
    from valueFileGrammar import globalGrammars
    grammarFinded = {} 

    name = input("Introducir el nombre de la gramatica: ")
    for grammar in globalGrammars:
        if name == grammar.getName():
            grammarFinded = grammar
            break

    grammarFinded.setTransitions()

    print("Transiciones: ")
    for transition in grammarFinded.getTransitions():
        print(transition["string"])
    
    grammarFinded = {}
    wait_for("", "\n")
    os.system('clear')
