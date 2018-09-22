class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def peek(self):
        if self.isEmpty():
            return
        return self.items[0]

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def display(self):
        for i in self.items:
            print(" {} ".format(i),end="-->")
        print("END")


myQueue = Queue()
for i in range(1,11):
    myQueue.enqueue(i)

myQueue.display()

for i in range(1,10):
    print(myQueue.dequeue())
    print(myQueue.peek())
    myQueue.display()

