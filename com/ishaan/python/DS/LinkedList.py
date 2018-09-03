class Node:

    def __init__(self,name):
        self.name = name
        self.next = None

    def getName(self):
        return self.name

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert(self,name):
        newNode = Node(name)
        curr = self.head
        if curr == None:
            self.head = newNode
            return self.head
        while ( curr.next != None):
            curr = curr.next
        curr.next = newNode

    def printLL(self):
        curr = self.head
        while(curr != None):
            print(curr.name)
            curr = curr.next


ll = LinkedList()
ll.insert("A")
ll.insert("B")
ll.insert("C")
ll.insert("D")
ll.insert("E")
ll.insert("F")
ll.insert("G")
ll.insert("H")
ll.printLL()
print("Answer is " + ll.head.next.next.next.name)


