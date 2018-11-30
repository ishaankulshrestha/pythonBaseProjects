from random import randint

my_list = []

counter = 0

while 1:
    num = randint(1,100)
    if num not in my_list:
        my_list.append(num)
        counter += 1
    if counter >= 20:
        break

print(my_list)


highest = 101
sec_highest = 101

for num in range(20):
    if my_list[num] < highest:
        sec_highest = highest
        highest = my_list[num]
        continue
    if my_list[num] < sec_highest and my_list[num] != highest:
        sec_highest = my_list[num]

print(sec_highest)
print(sorted(my_list,reverse=True))




