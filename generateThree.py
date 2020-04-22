from graphviz import Digraph

def generateThree(grammar, string):
    
    dot = Digraph(comment=f"{grammar.getName()}", format="png")
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='circle')
    dot.node(grammar.getNTInitial())

    grammar.get
    
    for letter in string:
        beforeLetter = letter
        if letter in grammar.getTerminals():
            dot.node(letter)
    
    dot.render(filename="three")
     