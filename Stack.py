class Stack():
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def getLastItems(self):
        return self.items[len(self.items)-1]
    
    def getItems(self):
        return self.items

    def searchIndexById(self, id):
        return self.items.index(id)

    def getLength(self):
        return len(self.items)