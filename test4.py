from AP import AP
from generateThree import generateThree
from generateReport import generateReport

ap = AP("ap1")

ap.setNonTerminals("S")
ap.setNonTerminals("T") # T
ap.setNonTerminals("E") # E
ap.setNonTerminals("F")
ap.setNonTerminals("R") # TP
ap.setNonTerminals("W") # EP

ap.setTerminals("+")
ap.setTerminals("-")
ap.setTerminals("*")
ap.setTerminals("/")
ap.setTerminals("n") # numero
ap.setTerminals("c") # cadena

ap.setNTInitial("S")

ap.setProductions("S>E")
ap.setProductions("E>TW")
ap.setProductions("W>+TW")
ap.setProductions("W>-TW")
ap.setProductions("W>epsilon")
ap.setProductions("T>FR")
ap.setProductions("R>/FR")
ap.setProductions("R>*FR")
ap.setProductions("R>epsilon")
ap.setProductions("F>n")
ap.setProductions("F>c")

ap.setTransitions()

# Mostrar Gramatica
# print(ap.getGrammar())

# Evaluar Cadenas
print(ap.generateAP("c/n*n+c"))

# Mostrar Arbol
# generateThree(ap, "zazabzbz")

# Generar Reportes
# generateReport(ap, "zazabzbz")