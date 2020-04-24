from Stack import Stack

class AP():

    name = ""
    non_terminals = []
    terminals = []
    non_terminal_initial = ""
    productions = []
    transitions = []
    firstOutput_lastInput = []
    
    def __init__(self, name):
        self.name = name

    def setNonTerminals(self, nt):
        self.non_terminals.append(nt)

    def setTerminals(self, t):
        self.terminals.append(t)

    def setNTInitial(self, ntI):
        self.non_terminal_initial = ntI

    def setProductions(self, prod):
        nt = prod.split(">")[0]
        prods = prod.split(">")[1]
        
        production = {
            "NT": nt,
            "prod": prods,
            "string": f"{nt}>{prods}"
        }
        self.productions.append(production)

    def deleteProductions(self, prodInput):
        for prod in self.productions:
            if prodInput == prod["string"]:
                prodInput = prod
                self.productions.remove(prodInput)

    def createTransition(self):
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

        return transition

    def setTransitions(self):
        for item in self.productions:
            
            transition = self.createTransition()

            # Establece transicion para prod. inicial
            if (item["NT"] == self.non_terminal_initial):
                self.setInitialTransition(transition, item)
                transition = self.createTransition()

            self.setSecondTransition(transition, item)
            transition = self.createTransition()
        self.setThirdTransitions(transition)
    
    def setInitialTransition(self, transition, item):
        transition["first"]["from"] = "p"
        transition["first"]["readed"] = "epsilon"
        transition["first"]["output"] = "epsilon"
        transition["last"]["to"] = "q"
        transition["last"]["input"] = item["NT"]
        transition["string"] = f"p,epsilon,epsilon;q,{item['NT']}"
        firstTransition = transition
        self.transitions.append(firstTransition)
        # self.firstOutput_lastInput.append()

    def setSecondTransition(self, transition, item):
        transition["first"]["from"] = "q"
        transition["first"]["readed"] = "epsilon"
        transition["first"]["output"] = item["NT"]
        transition["last"]["to"] = "q"
        transition["last"]["input"] = item["prod"]
        transition["string"] = f"q,epsilon,{item['NT']};q,{item['prod']}"
        secondTransition = transition
        self.transitions.append(secondTransition)

    def setThirdTransitions(self, transition):
        for item in self.terminals:
            transition["first"]["from"] = "q"
            transition["first"]["readed"] = item
            transition["first"]["output"] = item
            transition["last"]["to"] = "q"
            transition["last"]["input"] = "epsilon"
            transition["string"] = f"q,{item},{item};q,epsilon"
            thirdTransition = transition
            self.transitions.append(thirdTransition)
            transition = self.createTransition()

    def generateAP(self, string):
        stack = Stack()
        marker = True
        returnTransition = []
        returnProductions = []

        # print(f"Cadena a evaluar: {string}")
        # print(f"En la pila hay {stack.getItems()}")

        for transition in self.transitions:
            if transition["first"]["from"] == "p":
                stack.push(transition["last"]["input"])
                break

        for letter in string:
            if letter in self.terminals:
                for transition in self.transitions:
                    if transition["first"]["from"] == "q":
                        if stack.getLastItem() == transition["first"]["output"]:
                            stack.pop()
                            word = transition["last"]["input"][::-1]
                            for l in word:
                                stack.push(l)
                            # print(f"Pila actual: {stack.getItems()}")
                            returnTransition.append(stack.getLastItem())
                            
                            if stack.getItems() == 'epsilon':
                                marker = False
                                # print("Cadena Invalida")
                                # returnTransition.append("Cadena Invalida")
                                break
                        else:
                            for trans in self.transitions:
                                if (trans["first"]["output"] == stack.getLastItem()): 
                                    
                                    if (letter == trans["last"]["input"][0]):
                                        stack.pop()
                                        word = trans["last"]["input"][::-1]
                                        for l in word:
                                            stack.push(l)
                                        # print(f"Pila actual: {stack.getItems()}")
                                        returnTransition.append(stack.getLastItem())
                                        break

                                    if trans["last"]["input"] == 'epsilon':
                                        stack.pop()
                                        break

                                    if trans["last"]["input"] in self.non_terminals:
                                        stack.pop()
                                        stack.push(trans["last"]["input"])
                                        break
                        break

                    # print(f"Pila actual: {stack.getItems()}")
                    returnTransition.append(stack.getLastItem())

                    if stack.getItems() == 'epsilon':
                        marker = False
                        # print("Cadena Invalida")
                        # returnTransition.append("Cadena Invalida")
                        break

                if marker == False:
                    break

                if letter == stack.getLastItem():
                    if stack.getLength() > 1:
                        stack.pop()
            else:
                print(f"La letra {letter} no existe en el alfabeto")
                returnTransition.append("Cadena Invalida")
                break
        
        # if marker:
            # print('Cadena Valida')
            # returnTransition.append("Cadena Valida")
        
        # elementsForReport.append(elementsOfStack)
        return returnTransition

    def arrayOfTopStack(self, array):
        return array

    def getName(self):
        return self.name

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

    def getGrammar(self):
        stringStatus = "Estados: [p, q]\n"
        stringNT = f"No Terminales: {self.non_terminals} \n"
        stringT = f"Terminales: {self.terminals} \n"
        stringNTI = f"Terminal inicial: {self.non_terminal_initial} \n"
        stringProds = ""
        stringTrans = ""

        i = 1
        for prod in self.productions:
            stringProds += f"Produccion {i}: {prod['string']}\n"
            i = i + 1

        i = 1
        for transition in self.transitions:
            stringTrans += f"Transicion {i}: {transition['string']}\n"
            i = i + 1
            
        return f"{stringStatus}{stringNT}{stringT}{stringNTI}\n{stringProds}\n{stringTrans}"
