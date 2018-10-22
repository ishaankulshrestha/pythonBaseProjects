import heapq
from random import randint

myList = []
for i in range(20):
    myList.append(randint(1, 100))

print("{}".format(myList))

heapq.heapify(myList)

print("{}".format(myList))

for i in range(5):
    n = randint(200,300)
    print("appending {}".format(n))
    heapq.heappush(myList,n)

## following can be quite imporatant function of heap
## this replaces smallest with new.
heapq.heapreplace(myList,0)

print("\n10th largest value in above is {}".format(heapq.nlargest(10,myList)))

print("\n10th smallest value in above is {}".format(heapq.nsmallest(10,myList)))

print("\nfollowing is the popped result from the heap so formed.")

for i in range(len(myList)):
    print("{}".format(heapq.heappop(myList)), end= ", ")

## is a function heapq.nlargest(n,mylist)


