import heapq
from random import randint

my_dict = {3:"a",4:"b",45:"g",98:"t",43:"f",1:"k"}

print(my_dict)

my_list =[]

for k,v in my_dict.items():
    my_list.append((-k,v))
    if k%2 == 0:
        my_list.append((-k, v))

heapq.heapify(my_list)

print(my_list)

while my_list != []:
    n = heapq.heappop(my_list)
    print("{},{}".format(-n[0],n[1]))





