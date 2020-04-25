from AP import AP
from generateThree import generateThree
from generateReport import generateReport

ap = AP("ap1")

ap.setNonTerminals("S")
ap.setNonTerminals("E")
ap.setNonTerminals("Z")
ap.setNonTerminals("T")
ap.setNonTerminals("F")
ap.setNonTerminals("Y")

ap.setTerminals("a")
ap.setTerminals("b")
ap.setTerminals("c")
ap.setTerminals("d")
ap.setTerminals("n")
ap.setTerminals("h")

ap.setNTInitial("S")

ap.setProductions("S>E")
ap.setProductions("E>TZ")
ap.setProductions("Z>aTZ")
ap.setProductions("Z>bTZ")
ap.setProductions("Z>epsilon")
ap.setProductions("T>FY")
ap.setProductions("Y>cFY")
ap.setProductions("Y>dFY")
ap.setProductions("Y>epsilon")
ap.setProductions("F>n")
ap.setProductions("F>h")

ap.setTransitions()

# Mostrar Gramatica
# print(ap.getGrammar())

# Evaluar Cadenas
print(ap.generateAP("ndnanch"))

# Mostrar Arbol
# generateThree(ap, "zazabzbz")

# Generar Reportes
# generateReport(ap, "zazabzbz")