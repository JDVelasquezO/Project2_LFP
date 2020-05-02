content = "digraph G{\nrankdir=TB; node[shape=record];"
counter = -1

def generateTree(parent, value, objects):
    if parent == "":
        counter = counter + 1
        content += "\ninicio" + value + " [label = " + value + " ];"

        for item in objects:
            counter = counter + 1
            if type(item) == type(str):
                content += "\nnodo" + content + "[label = " + item + "];\ninicio" + value + "-> nodo" + counter + ";"
            else:
                production = item
                generateTree(value, production.value, production.childrens)
    else:
        if parent == value:
            counter = counter + 1
            content += "\ninicio" + value + 2 +" [label = " + value + 2+" ];\ninicio" + parent + "->inicio" + value + 2 + ";"
            for item in objects:
                counter = counter + 1
                if type(item) == type(str):
                    content += "\nnodo" + counter + "[label = " + item + "];\ninicio" + value + 2 + "-> nodo" + counter + ";"
                else:
                    production = item
                    generateTree(production.parent.value, production.value, production.childrens)
        else:
            counter = counter + 1
            content += "\ninicio" + value + " [label = " + value + " ];\ninicio" + parent + "->inicio" + value + ";"
            for item in objects:
                counter = counter + 1 
                if (type(item) == type(str)):
                    content += "\nnodo" + counter + "[label = " + item + "];\ninicio" + value + "-> nodo" + counter + ";"
                else:
                    production = item
                    generateTree(production.parent.value, production.value, production.childrens)