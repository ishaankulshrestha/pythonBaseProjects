import sys
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

def percolatedown(heaplist,i):
    if 2*i > (len(heaplist)-1) :
        return
    if 2*i == len(heaplist) - 1 :
        if heaplist[2*i] < heaplist[i]:
            swap(heaplist,2*i,i)
        return
    try:
        if heaplist[i] > heaplist[i*2 +1] > heaplist[i*2]:
            swap(heaplist,i*2,i)
            percolatedown(heaplist,i*2)
        if heaplist[i] > heaplist[i*2] > heaplist[i*2+1]:
            swap(heaplist,i*2+1,i)
            percolatedown(heaplist,i*2+1)
        if heaplist[i*2] > heaplist[i] > heaplist[i*2+1]:
            swap(heaplist,i*2+1,i)
            percolatedown(heaplist,i*2+1)
        if heaplist[i*2+1] > heaplist[i] > heaplist[i*2]:
            swap(heaplist,i*2,i)
            percolatedown(heaplist,i*2)
        return
    except:
        print("i = {} length = {}".format(i,len(my_list)))
        sys.exit()


def heappop(heaplist):
    answer = heaplist[1]
    heaplist[1] = heaplist[len(heaplist)-1]
    del heaplist[len(heaplist)-1]
    percolatedown(heaplist,1)
    return answer




## In order Traversal of BST should give sorted data
def heapprint(heaplist):
    #print(heaplist)
    k = 1
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




## Main programme

my_list = [0]


counter = 0

while True:
    n = randint(1,35)
    if n not in my_list:
        heappush(my_list,n)
       # heapprint(my_list)

       # _ = input()
       # os.system('export TERM=xterm')
        #os.system('clear')
        counter += 1
        if counter >= 35:
            break


while my_list != [0]:
    print(heappop(my_list),end=" ")
    #heapprint(my_list)
    #_ = input()








