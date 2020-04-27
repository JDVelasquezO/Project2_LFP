from AP import AP
from generateThree import generateThree
from generateReport import generateReport

ap = AP("ap1")

ap.setNonTerminals("S")
ap.setNonTerminals("M")
ap.setNonTerminals("N")

ap.setTerminals("a")
ap.setTerminals("b")
ap.setTerminals("z")

ap.setNTInitial("S")

ap.setProductions("S>z M N z")
ap.setProductions("M>a M a")
ap.setProductions("M>z")
ap.setProductions("N>b N b")
ap.setProductions("N>z")
ap.setProductions("M>N z a")

ap.deleteProductions("M>N z a")

ap.setTransitions()

# Mostrar Gramatica
# print(ap.getGrammar())

# Evaluar Cadenas
print(ap.generateAP("zazabzbz"))
# ap.generateAP("zazabzbz")

# Mostrar Arbol
# generateThree(ap, "zazabzbz")

# Generar Reportes
# generateReport(ap, "zazabzbz")