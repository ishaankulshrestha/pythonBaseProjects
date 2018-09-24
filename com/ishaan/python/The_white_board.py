from random import randint


def bubble_sort(mylist):
    for i in range(len(mylist) - 1, -1, -1):
        for j in range(0, i):
            if mylist[i] < mylist[j]:
                temp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = temp


mylist = []

for i in range(20):
    mylist.append(randint(1, 100))

print(mylist)
bubble_sort(mylist)
print(mylist)

