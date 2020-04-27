from AP import AP
from generateThree import generateThree
from generateReport import generateReport

ap = AP("ap1")

ap.setNonTerminals("S")
ap.setNonTerminals("E")
ap.setNonTerminals("T")
ap.setNonTerminals("EP")
ap.setNonTerminals("TP")
ap.setNonTerminals("F")

ap.setTerminals("+")
ap.setTerminals("-")
ap.setTerminals("*")
ap.setTerminals("/")
ap.setTerminals("numero")
ap.setTerminals("cadena")

ap.setNTInitial("S")

ap.setProductions("S>E")
ap.setProductions("E>T EP")
ap.setProductions("EP>+ T EP")
ap.setProductions("EP>- T EP")
ap.setProductions("EP>epsilon")
ap.setProductions("T>F TP")
ap.setProductions("TP>/ F TP")
ap.setProductions("TP>* F TP")
ap.setProductions("TP>epsilon")
ap.setProductions("F>numero")
ap.setProductions("F>cadena")

ap.setTransitions()

# Mostrar Gramatica
# print(ap.getGrammar())

# Evaluar Cadenas
print(ap.generateAP("cadena / numero * numero + cadena"))

# Mostrar Arbol
# generateThree(ap, "zazabzbz")