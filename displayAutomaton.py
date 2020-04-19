import os
from createGrammar import globalGrammar
from press_enter import wait_for
from graphviz import Digraph

def displayAutomaton(self):
    
    grammarFinded = {}

    name = input("Introducir el nombre de la gramatica: ")
    for grammar in globalGrammar:
        if name == grammar.getName():
            grammarFinded = grammar
            break
    
    dot = Digraph(comment="automata_pila", filename="ap.gv")
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='doublecircle')
    dot.node('f')

    dot.attr('node', shape='circle')
    dot.edge('i', 'p', 'Inicio')

    for trans in grammarFinded.getTransitions():
        dot.edge(trans["first"]["from"], trans["last"]["to"], trans["last"]["input"])

    dot.edge('q', 'f', 'epsilon;S;epsilon')

    dot.view()