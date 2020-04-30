from AP import AP
from createGrammar import globalGrammar

def valueFileGrammar(name, file):
    
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    
    ap = AP(name)
    globalGrammar.append(ap)

    lines = file.read().split("\n")
    non_terminals = []
    terminals = []
    productions = []

    productions = lines

    for line in lines:
        non_terminals.append(line.split(">")[0])

        produceds = line.split(">")[1]
        produced = produceds.split(" ")

        for prod in produced:
            if prod in lowercase:
                terminals.append(prod)
    
    non_terminal_initial = lines[0][0]
    non_terminals = set(non_terminals)
    terminals = set(terminals)

    ap.setNonTerminals = non_terminals
    ap.setTerminals = terminals
    ap.setProductions = productions
    ap.setNTInitial = non_terminal_initial
    # print(non_terminals)
     