class heap(object):

    def __init__(self):
        self.arr = []
        self.heapsize = 0

    def display(self):
        j = 0
        w = 50
        for i in self.arr :
            for _ in range(50 - (2**j + 1)//2):
                print(" "*(50 - (2**j + 1)))
            for k in range(2**j + 1):
                print(" {} ".format(self.arr[i+k]),end=" ")




heap_nw = heap()
for i in range(1,11,2):
    heap_nw.arr.append(i)
heap_nw.display()

for i in range(1,11,2):
    heap_nw.arr.append(i)
heap_nw.display()

