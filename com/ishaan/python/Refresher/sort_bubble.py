from random import randint

## Implementing Bubble sort. The simplest sorting algorithm.

def check_sorted(arr):
    temp = arr[0]
    for i in arr:
        if i < temp:
            return False
        temp = i
    return True


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

print("The sorted flag is {} and list is \n{},".format(check_sorted(mylist), mylist))

bubble_sort(mylist)

print("The sorted flag is {} and list is \n{},".format(check_sorted(mylist), mylist))