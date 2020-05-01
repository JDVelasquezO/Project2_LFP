from AP import AP
from createGrammar import globalGrammar

def valueFileGrammar(name, file):
    
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '+-*/()?¿'
    
    ap = AP(name)
    globalGrammar.append(ap)

    lines = file.read().split("\n")
    productions = []

    productions = lines

    for line in lines:

        if line != '':
            nt = line.split(">")[0]
            if nt in capital_letters:
                if nt not in ap.getNonTerminals():
                    ap.setNonTerminals(nt)

            produceds = line.split(">")[1]
            produced = produceds.split(" ")

            for prod in produced:
                if prod not in capital_letters:
                    if prod in symbols or prod != 'epsilon':
                        if prod not in ap.getTerminals():
                            ap.setTerminals(prod)
    
    ap.setNTInitial(lines[0][0])

    for line in lines:
        if line != '':
            ap.setProductions(line)
    print('Gramatica Guardada')
     