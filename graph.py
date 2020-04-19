from graphviz import Digraph

dot = Digraph(comment="automata_pila", filename="ap.gv")
dot.attr(rankdir='LR', size='8,5')
dot.attr('node', shape='doublecircle')
dot.node('f')

dot.attr('node', shape='circle')
dot.edge('i', 'p', 'Inicio')
dot.edge('p', 'q', 'epsilon,epsilon;S')
dot.edge('q', 'q', 'epsilon,M;aMa')
dot.edge('q', 'q', 'epsilon,M;z')
dot.edge('q', 'q', 'epsilon,N;bNb')
dot.edge('q', 'q', 'epsilon,N;z')
dot.edge('q', 'q', 'b,b;epsilon')
dot.edge('q', 'q', 'a,a;epsilon')
dot.edge('q', 'q', 'z,z;epsilon')
dot.edge('q', 'f', 'epsilon;S;epsilon')

dot.view()