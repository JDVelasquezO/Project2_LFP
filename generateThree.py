from graphviz import Digraph

def generateThree(grammar, string):
    
    dot = Digraph(comment=f"{grammar.getName()}", format="png")
    dot.attr(rankdir='TB', size='8,5')
    dot.attr('node', shape='circle')
    # dot.node(grammar.getNTInitial())

    nodes = grammar.generateAP(string)
    arrayEdges = []
    print(nodes)

    i = 65
    for node in nodes:
        dot.node(chr(i), node)

        # if arrayEdges in grammar.getNonTerminals():
        #     arrayEdges.append()
        
        arrayEdges.append('A'+chr(i))

        i = i + 1

    dot.edges(['AB', 'AC', 'CD', 'CE', 'EF', 'CG', 'AH', 'HI', 'HJ', 'JK', 'HL', 'AM'])

    
    dot.render(filename="three")
     