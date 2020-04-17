from AP import AP

ap = AP("ap1")

ap.setNonTerminals("S")
ap.setNonTerminals("M")
ap.setNonTerminals("N")

ap.setTerminals("x")
ap.setTerminals("y")

ap.setNTInitial("S")

ap.setProductions("S>xMx")
ap.setProductions("M>xMx")
ap.setProductions("M>N")
ap.setProductions("N>yN")
ap.setProductions("N>epsilon")

ap.setTransitions()

ap.generateAP("xxxyyyyxxx")