from graphviz import Digraph

def generateThree(grammar, string):
    
    dot = Digraph(comment=f"{grammar.getName()}", format="png")
    dot.attr(rankdir='TB', size='8,5')
    dot.attr('node', shape='circle')
    # dot.node(grammar.getNTInitial())

    nodes = grammar.generateAP(string)
    arrayEdges = []
    print(nodes)

    # ['S', 'z', 'M', 'a', 'M', 'z', 'a', 'N', 'b', 'N', 'z', 'b', 'z']

    i = 65
    nodeTemp = ''
    relation = {}
    relations = []
    marker = False

    for node in nodes:
        dot.node(chr(i), node)
        arrayEdges.append(nodeTemp+chr(i))

        # if node in grammar.getNonTerminals():
        #     if nodeTemp != '':
        #         arrayEdges.append(nodeTemp+chr(i))
        #         pushRelations(relation, i, node, relations)
        #         relation = {}
        #     nodeTemp = chr(i)

        # if node in grammar.getTerminals():
        #     for production in grammar.getProductions():
        #         if production["prod"][0] == node:
        #             for rel in relations:
        #                 if rel['value'] == production['NT']:
        #                     arrayEdges.append(rel['key']+chr(i))
        #                     marker = True
        #                     break
                    
        #             if not marker:
        #                 arrayEdges.append(nodeTemp+chr(i))
        #                 pushRelations(relation, i, node, relations)
        #                 relation = {}
        #                 break
        #             break
        
        # else:
        #     if chr(i) != nodeTemp:
        #         arrayEdges.append(nodeTemp+chr(i))

        i = i + 1

    # dot.edges(['AB', 'AC', 'CD', 'CE', 'EF', 'CG', 'AH', 'HI', 'HJ', 'JK', 'HL', 'AM'])
    dot.edges(arrayEdges)
    
    dot.render(filename="three")

def pushRelations(relation, i, node, relations):
    relation['key'] = chr(i)
    relation['value'] = node
    relations.append(relation)
     