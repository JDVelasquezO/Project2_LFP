class Stack():
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def getLastItem(self):
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        else:
            return "epsilon"
    
    def getItems(self):
        if len(self.items) == 0:
            return "epsilon"
        return self.items

    def searchIndexById(self, id):
        return self.items.index(id)

    def getLength(self):
        return len(self.items)