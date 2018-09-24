from random import randint

## Implementing Bubble sort. The simplest sorting algorithm.

def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


mylist = []

for i in range(20):
    mylist.append(randint(1, 100))

print("The sorted values are as follows \n{}".format(mylist))

bubble_sort(mylist)

print("The sorted values are as follows \n{}".format(mylist))