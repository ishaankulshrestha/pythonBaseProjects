class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.isEmpty():
            return
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def display(self):
        for i in self.items:
            print(" {} ".format(i),end="-->")
        print("END")


myStack = Stack()
for i in range(1,11):
    myStack.push(i)

myStack.display()

for i in range(1,10):
    print(myStack.pop())
    print(myStack.peek())
    myStack.display()

