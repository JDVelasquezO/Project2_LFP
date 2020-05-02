from Production import Production
from generateTree import generateTree

def makeNodes():
    
    parent = Production("S")
    parent.childrens.append("z")
    parent.childrens.append(Production(parent, "M"))
    parent.childrens.append(Production(parent, "N"))
    parent.childrens.append("z")

    children = parent.childrens[1]
    children.childrens.append("a")
    children.childrens.append(Production(children, "M"))
    children.childrens.append("a")

    children2 = parent.childrens[2]
    children2.childrens.append("b")
    children2.childrens.append(Production(children2, "N"))
    children2.childrens.append("b")

    children3 = children.childrens[1]
    children3.childrens.append("z")
    children3.childrens.append(Production(children3, "M"))

    children4 = children3.childrens[1]
    children4.childrens.append("z")

    generateTree()

makeNodes()