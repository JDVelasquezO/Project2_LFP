
class Production():
    
    parent = ''
    childrens = []
    value = ''

    def __init__(self, parent, children = None):
        self.parent = parent
        self.childrens = []
        self.value = children