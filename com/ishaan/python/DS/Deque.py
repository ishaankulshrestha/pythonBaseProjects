class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def getSize(self):
        return len(self.items)

    def __str__(self):
        return str([x for x in self.items])

myDeque = Deque()

for i in range(10,0,-1):
    if i%2 != 0 :
        myDeque.addRear(i)
    else:
        myDeque.addFront(i)

for i in range(1,11):
    if i%2 != 0 :
        print(myDeque.removeRear())
    else :
        print(myDeque.removeFront())

