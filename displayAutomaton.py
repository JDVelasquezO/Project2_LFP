import os
# from createGrammar import globalGrammar
from press_enter import wait_for
from graphviz import Digraph

def displayAutomaton():
    
    from menu import globalGrammars
    grammarFinded = {}

    name = input("Introducir el nombre de la gramatica: ")
    for grammar in globalGrammars:
        if name == grammar.getName():
            grammarFinded = grammar
            break
    
    print(grammarFinded.getGrammar())
    
    dot = Digraph(comment=f"{grammarFinded.getName()}", format="png")
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')
    dot.node('f')

    dot.attr('node', shape='circle')
    dot.edge('i', 'p', f'{grammarFinded.getNTInitial()}')

    for trans in grammarFinded.getTransitions():
        firstState = trans["first"]["from"]
        lastState = trans["last"]["to"]
        string = trans["last"]["input"]
        result = f"{firstState},{lastState};{string}"

        dot.edge(firstState, lastState, label=result)

    dot.edge('q', 'f', f'epsilon,{grammarFinded.getNTInitial()};epsilon')

    dot.render(filename="ap")