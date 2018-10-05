import heapq
from random import randint

my_list = [0]*20
for i in range(20):
    my_list[i] = (randint(200,300))

print("original list is \n {}".format(my_list))

heapq.heapify(my_list)

print(" {}".format(my_list))

for i in range(20):
    num = randint(100,200)
    heapq.heappush(my_list,num)


print(" {}".format(my_list))

heapq.heapreplace(my_list,my_list[4])

#heapq.heappushpop(my_list,9)

print("after push and pop")


print(" {}".format(my_list))


sorted_list = []

for i in range(40):
    num = heapq.heappop(my_list)
    sorted_list.append(num)

print(sorted_list)


