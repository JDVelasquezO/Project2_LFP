from Stack import Stack
from graphviz import Digraph
import csv

class AP():

    name = ""
    non_terminals = []
    terminals = []
    non_terminal_initial = ""
    productions = []
    transitions = []
    firstOutput_lastInput = []

    myData = [
        ["PILA$ENTRADA$TRANSICION"]
    ]
    
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
        marker = True
        newProds = ''
        
        if len(prods.split(' ')) == 1:
            newProds += prods
        elif prods == 'epsilon':
            newProds += 'epsilon'
        else:
            for prod in prods:
                if prod in self.terminals or prod in self.non_terminals:
                    newProds += prod
        
        production = {
            "NT": nt,
            "prod": newProds,
            "string": f"{nt}>{newProds}"
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
        if firstTransition not in self.transitions:
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
        newTransition = ''
        newString = ''

        print(f"Cadena a evaluar: {string}")
        print(f"En la pila hay {stack.getItems()}")
        self.generateReport('epsilon', string, self.transitions[0]['string'])
        newString = string

        for transition in self.transitions:
            if transition["first"]["from"] == "p":
                stack.push(transition["last"]["input"])
                break

        newTransition = transition['string']

        if ' ' in string:
            string = string.split(' ')

        i = 0
        for letter in string:
            indicator = False
            if i >= 2:
                string = string[1:]
                newString = list(string)
                if len(string) > 0:
                    newString.pop(0)

            if letter in self.terminals:
                for transition in self.transitions:
                    if transition["first"]["from"] == "q":
                        if stack.getLastItem() == transition["first"]["output"]:
                            if letter == transition['last']['input'][0]:
                                newTransition = transition['string']
                                stack.pop()
                                word = transition["last"]["input"][::-1]
                                for l in word:
                                    indicator = True
                                    stack.push(l)
                                
                                if stack.getItems() == 'epsilon':
                                    marker = False
                                    print("Cadena Invalida")
                                    returnTransition.append("Cadena Invalida")
                                    break
                            else:
                                continue
                        else:
                            for trans in self.transitions:
                                if (trans["first"]["output"] == stack.getLastItem()):
                                    if (letter == trans["last"]["input"][0] or letter == trans["last"]["input"]):
                                        newTransition = trans['string']
                                        stack.pop()
                                        
                                        if len(letter) > 1:
                                            stack.push(letter)
                                        else:
                                            word = trans["last"]["input"][::-1]
                                            for l in word:
                                                stack.push(l)

                                        print(f"Pila actual: {stack.getItems()}")
                                        self.generateReport(stack.getItems(), newString, newTransition)
                                        returnTransition.append(stack.getLastItem())
                                        indicator = True
                                        break

                                    if trans["last"]["input"] == 'epsilon':
                                        newTransition = trans['string']
                                        self.generateReport(stack.getItems(), newString, newTransition)
                                        stack.pop()
                                        indicator = True
                                        break

                                    if trans["last"]["input"][0] in self.non_terminals:
                                        newTransition = trans['string']
                                        self.generateReport(stack.getItems(), newString, newTransition)
                                        stack.pop()
                                        for l in trans["last"]["input"][::-1]:
                                            stack.push(l)
                                        indicator = True
                                        break
                            
                            if not indicator:
                                marker = False
                                break

                            if letter == stack.getLastItem():
                                break

                            if trans['first']['output'] == letter:
                                break

                    print(f"Pila actual: {stack.getItems()}")
                    returnTransition.append(stack.getLastItem())
                    # self.generateReport(stack.getItems(), newString, newTransition)

                    # if not indicator:
                    #     marker = False
                    #     break

                    if stack.getItems() == 'epsilon':
                        marker = False
                        print("Cadena Invalida")
                        returnTransition.append("Cadena Invalida")
                        break

                if marker == False:
                    break

                if letter == stack.getLastItem():
                    if stack.getLength() > 1:
                        stack.pop()

                if len(stack.getItems()) == 0:
                    break

            else:
                print(f"La letra {letter} no existe en el alfabeto")
                returnTransition.append("Cadena Invalida")
                break

            i = i + 1

        if marker:
            if len(stack.getItems()) > 0:
                while True:
                    if len(stack.getItems()) == 0:
                        break
                    for trans in self.transitions:

                        if (trans["first"]["output"] == stack.getLastItem()):
                            if trans['first']['readed'] == 'epsilon' and trans['last']['input'] == 'epsilon':
                                print(f"Pila actual: {stack.getItems()}")
                                returnTransition.append(stack.getLastItem())
                                newTransition = trans['string']
                                self.generateReport(stack.getItems(), '--------', newTransition)
                                stack.pop()
                                break

        if marker:
            print('Cadena Valida')
            returnTransition.append("Cadena Valida")

            if len(stack.getItems()) == 0:
                self.generateReport('epsilon', '---------', 'q,epsilon,epsilon;f,epsilon')
                self.generateReport('-------', '---------', 'Aceptacion')
            else:
                self.generateReport(stack.getItems(), string, 'Aceptacion')
        else:
            print("Cadena Invalida")

        return returnTransition

    def generateReport(self, eStack, eInput, eTransition):
        array = []
        string = f"{eStack}${eInput}${eTransition}"
        array.append(string)

        self.myData.append(array)

        myFile = open('report.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(self.myData)
        myFile.close()

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
