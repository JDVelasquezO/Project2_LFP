from AP import AP
from createGrammar import globalGrammar

def valueFileGrammar(name, file):
    
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    
    ap = AP(name)
    globalGrammar.append(ap)

    lines = file.read().split("\n")
    productions = []

    productions = lines

    for line in lines:
        nt = line.split(">")[0]
        if nt not in ap.getNonTerminals():
            ap.setNonTerminals(nt)

        produceds = line.split(">")[1]
        produced = produceds.split(" ")

        for prod in produced:
            if prod in lowercase:
                if prod not in ap.getTerminals():
                    ap.setTerminals(prod)
    
    ap.setNTInitial(lines[0][0])

    for line in lines:
        ap.setProductions(line)
    print('Gramatica Guardada')
     