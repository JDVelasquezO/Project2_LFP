from AP import AP

ap = AP("ap1")

ap.setNonTerminals("S")
ap.setNonTerminals("M")
ap.setNonTerminals("N")

ap.setTerminals("x")
ap.setTerminals("y")

ap.setNTInitial("S")

ap.setProductions("S>x M x")
ap.setProductions("M>x M x")
ap.setProductions("M>N")
ap.setProductions("N>y N")
ap.setProductions("N>epsilon")

ap.setTransitions()

# print(ap.getGrammar())

print(ap.generateAP("xxxyyyyxxx"))
# ap.generateAP("xxxyyyyxxyx")