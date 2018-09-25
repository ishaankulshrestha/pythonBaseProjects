def search_postion(arr,key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i+1
    return 0


mylist = [14, 52, 27, 34, 35, 25, 24, 79, 41, 55, 92, 5, 46, 23, 2, 5, 54, 45, 84, 46]
x , y = 52,53
get_position = search_postion(mylist,x)

print("List is {} ".format(mylist))

if (get_position):
    print("{} exists in the list at position {}".format(x,get_position))
else:
    print("{} do not exists in the list".format(x))

get_position = search_postion(mylist,y)

if (get_position):
    print("{} exists in the list at position".format(x,get_position))
else:
    print("{} do not exists in the list".format(x))

