class AP():

    name = ""
    non_terminals = []
    terminals = []
    non_terminal_initial = ""
    productions = []
    transitions = []
    
    def __init__(self, name):
        self.name = name

    def setNonTerminals(self, nt):
        self.non_terminals.append(nt)

    def setTerminals(self, t):
        self.terminals.append(t)

    def setNTInitial(self, ntI):
        self.non_terminal_initial = ntI

    def setProductions(self, prod):
        self.productions.append(prod)

    def setTransitions(self):
        for item in self.productions:
            
            transition = { #Por cada produccion se crea una transicion básica
                "first": {
                    "from": "",
                    "readed": "",
                    "output": ""
                },

                "last": {
                    "to": "",
                    "input": ""
                },

                "string": ""
            }

            # Establece transicion para prod. inicial
            if (item[0] == self.non_terminal_initial):
                self.setInitialTransition(transition, item[0])
    
    def setInitialTransition(self, transition, item):
        transition["first"]["from"] = "p"
        transition["first"]["readed"] = "epsilon"
        transition["first"]["output"] = "epsilon"
        transition["last"]["to"] = "q"
        transition["last"]["input"] = item
        transition["string"] = f"p,epsilon,epsilon;q,{item}"
        initialTransition = transition
        self.transitions.append(initialTransition)        

    def getNonTerminals(self):
        return self.non_terminals

    def getTerminals(self):
        return self.terminals

    def getNTInitial(self):
        return self.non_terminal_initial

    def getProductions(self):
        return self.productions

    def getTransitions(self):
        return self.transitions
