
class Production():
    
    parent = ''
    childrens = []
    value = ''

    def __init__(self, parent, children):
        self.parent = parent
        self.childrens = []
        self.value = children

    def __init__(self, value):
        self.value = value
        self.childrens = []
