import os
from random import randint
import math

def heapify(root):
    pass


def generate_space():
    for i in range(1000):
        yield 2**i

## Insertion in BST Random
def heappush(heaplist,n):
    heaplist.append(n)
    percolateup(heaplist,len(heaplist)-1)
    return heaplist

def swap(root,a,b):
    temp = root[a]
    root[a] = root[b]
    root[b] = temp

def percolateup(heaplist,i):
    if heaplist[i] >= heaplist[i//2]:
        return
    swap(heaplist,i,i//2)
    percolateup(heaplist,i//2)

# def percolatedown(root,i):
#     if i > root.size//2:
#         return
#     if i == root.size/2:
#         if root[i] > root[i/2]:
#             swap(root,i,i//2)
#             return
#     if root[i*2] > root[i*2 + 1] and root[i] <
#     temp = root[i//2]
#     root[i//2] = root[i]
#     root[i] = temp
#     percolateup(root,i//2)



## In order Traversal of BST should give sorted data
def heapprint(heaplist):
    print(heaplist)
    k = 0
    gen = generate_space()
    for i in range(math.ceil(math.log(len(heaplist),2))+1):
        numb = next(gen)
        #print(numb)
        print("  "*(40-numb*2),end="")
        for j in range(numb):
            if k >= len(heaplist):
                break
            print("{}    ".format(heaplist[k]),end=" ")
            k += 1
        print("\n")


    pass

## Level order traversal for BST
def heappop(root):
    pass


## Main programme

my_list = []


counter = 0

while True:
    n = randint(1,35)
    if n not in my_list:
        heappush(my_list,n)
        heapprint(my_list)

        _ = input()
       # os.system('export TERM=xterm')
        #os.system('clear')
        counter += 1
        if counter >= 35:
            break


#Arunesh now








