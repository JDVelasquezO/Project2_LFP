from AP import AP
from graphviz import Digraph

ap = AP("ap1")

ap.setNonTerminals("S")
ap.setNonTerminals("M")
ap.setNonTerminals("N")

ap.setTerminals("a")
ap.setTerminals("b")
ap.setTerminals("z")

ap.setNTInitial("S")

ap.setProductions("S>zMNz")
ap.setProductions("M>aMa")
ap.setProductions("M>z")
ap.setProductions("N>bNb")
ap.setProductions("N>z")
ap.setProductions("M>Nza")

ap.deleteProductions("M>Nza")

ap.setTransitions()

# Evaluar Cadenas
# ap.generateAP("zazabzbz")
# ap.generateAP("zzzzzzazabzbz")

print(ap.getGrammar())

# dot = Digraph(comment="automata_pila", filename="ap.gv")
# dot.attr(rankdir='LR', size='8,5')
# dot.attr('node', shape='doublecircle')
# dot.node('f')

# dot.attr('node', shape='circle')
# dot.edge('i', 'p', 'Inicio')

# for trans in ap.getTransitions():
#     firstState = trans["first"]["from"]
#     lastState = trans["last"]["to"]
#     string = trans["last"]["input"]
#     result = f"{firstState},{lastState};{string}"
#     dot.edge(firstState, lastState, label=result)

# dot.edge('q', 'f', 'epsilon,S;epsilon')

# dot.view()