
def getfriends(passed_list):
    my_dict = dict()
    for pair in passed_list:
        if len(pair) == 2:
            for ele in pair:
                my_dict[ele] = my_dict.get(ele,0) + 1
        else:
            for ele in pair:
                my_dict[ele] = 0
    return  my_dict


print(getfriends([['A','B'],['B','C'],['B','D'],['E']]))