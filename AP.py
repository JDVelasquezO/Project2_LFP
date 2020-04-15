class AP():

    name = ""
    non_terminals = []
    terminals = []
    non_terminal_initial = ""
    transitions = []
    
    def __init__(self, name):
        self.name = name

    def setNonTerminals(self, nt):
        self.non_terminals.append(nt)

    def setTerminals(self, t):
        self.terminals.append(t)

    def setNTInitial(self, ntI):
        self.non_terminal_initial = ntI

    def setTransitions(self, transition):
        self.transitions.append(transition)

    def getNonTerminals(self):
        return self.non_terminals

    def getTerminals(self):
        return self.terminals

    def getNTInitial(self):
        return self.non_terminal_initial

    def getTransitions(self):
        return self.transitions
