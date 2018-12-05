def binary_search(arr,start_position,end_position,key):
    mid_position = (start_position + end_position)//2
    if arr[mid_position] == key:
        return mid_position + 1
    if arr[mid_position] < key:
        start_position = mid_position +1
    else:
        end_position = mid_position -1
    if start_position > len(arr) - 1 or end_position < 0 or start_position > end_position:
        return 0
    return binary_search(arr,start_position,end_position,key)

s


sorted_mylist = [2, 5, 5, 14, 23, 24, 25, 27, 34, 35, 41, 45, 46, 46, 52, 54, 55, 79, 84, 92, 99]

for x in sorted_mylist:
    x = x + 1
    start_position = 0
    end_position = len(sorted_mylist) - 1

    get_position = binary_search(sorted_mylist, start_position, end_position, x)

    #print("List is {} ".format(mylist))

    if (get_position):
        print("{} exists in the list at position {}".format(x,get_position))
    else:
        print("{} do not exists in the list".format(x))

    # start_position = 0
    # end_position = len(mylist)-1

# get_position = binary_search(mylist,start_position,end_position,y)
#
# if (get_position):
#     print("{} exists in the list at position".format(y,get_position))
# else:
#     print("{} do not exists in the list".format(y))





