from AP import AP
from generateThree import generateThree
from displayAutomaton import displayAutomaton

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

# print(ap.getGrammar())
# Evaluar Cadenas
# print(ap.generateAP("zazabzbz"))
ap.generateAP("zazabzbz")
# generateThree(ap, "zazabzbz")