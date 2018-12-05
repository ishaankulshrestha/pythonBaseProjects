from random import randint
import heapq

my_list = []
heap_list = []

counter = 0

while 1:
    num = randint(1,100)
    if num not in my_list:
        my_list.append(num)
        counter += 1
    if counter >= 20:
        break

print(my_list)

highest = -100
ten_highest = -100

for num in range(20):
    heapq.heappush(heap_list,my_list[num])
    if len(heap_list) > 10 :
        heapq.heappop(heap_list)

ten_highest = heapq.heappop(heap_list)


print(ten_highest)
print(sorted(my_list,reverse=True))




