from random import randint


# Following program sort a list using insertion sort

def check_sorted(arr):
    temp = arr[0]
    for i in arr:
        if i < temp:
            return False
        temp = i
    return True


def insertion_sort(arr):
    for i in range(len(arr)):
        current = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = current
                break
            if j == 0:
                arr[0] = current


mylist = []

for i in range(20):
    mylist.append(randint(1, 100))

print("The sorted flag is {} and list is \n{} \n\n".format(check_sorted(mylist), mylist))

insertion_sort(mylist)

print("The sorted flag is {} and list is \n{},".format(check_sorted(mylist), mylist))


