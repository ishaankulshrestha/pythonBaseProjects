from random import randint


## Following program sort a list using selection sort

def check_sorted(arr):
    temp = arr[0]
    for i in arr:
        if i < temp:
            return False
        temp = i
    return True


def selection_sort(arr):
    for i in range(len(arr)):
        min_position = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_position]:
                min_position = j
        if min_position != i:
            temp = arr[i]
            arr[i] = arr[min_position]
            arr[min_position] = temp


mylist = []

for i in range(20):
    mylist.append(randint(1, 100))

print("The sorted flag is {} and list is \n{},".format(check_sorted(mylist), mylist))

selection_sort(mylist)

print("The sorted flag is {} and list is \n{},".format(check_sorted(mylist), mylist))