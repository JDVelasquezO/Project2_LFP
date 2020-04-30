from AP import AP
from generateThree import generateThree
from generateReport import generateReport

ap = AP("ap1")

ap.setNonTerminals("S")

ap.setTerminals("a")
ap.setTerminals("b")
ap.setTerminals("c")

ap.setNTInitial("S")

ap.setProductions("S>a S a")
ap.setProductions("S>b S b")
ap.setProductions("S>c")

ap.setTransitions()

# Mostrar Gramatica
# print(ap.getGrammar())

# Evaluar Cadenas
print(ap.generateAP("abacaba"))

# Mostrar Arbol
# generateThree(ap, "zazabzbz")