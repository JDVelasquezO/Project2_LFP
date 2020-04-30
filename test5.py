from AP import AP
from generateThree import generateThree
from generateReport import generateReport

ap = AP("ap1")

ap.setNonTerminals("S")
ap.setNonTerminals("E")
ap.setNonTerminals("T")
ap.setNonTerminals("W") # EP
ap.setNonTerminals("Y") # TP
ap.setNonTerminals("F")

ap.setTerminals("+")
ap.setTerminals("-")
ap.setTerminals("*")
ap.setTerminals("/")
ap.setTerminals("numero")
ap.setTerminals("cadena")

ap.setNTInitial("S")

ap.setProductions("S>E")
ap.setProductions("E>T W")
ap.setProductions("W>+ T W")
ap.setProductions("W>- T W")
ap.setProductions("W>epsilon")
ap.setProductions("T>F Y")
ap.setProductions("Y>/ F Y")
ap.setProductions("Y>* F Y")
ap.setProductions("Y>epsilon")
ap.setProductions("F>numero")
ap.setProductions("F>cadena")

ap.setTransitions()

# Mostrar Gramatica
# print(ap.getGrammar())

# Evaluar Cadenas
print(ap.generateAP("cadena * cadena + numero - cadena"))

# Mostrar Arbol
# generateThree(ap, "zazabzbz")