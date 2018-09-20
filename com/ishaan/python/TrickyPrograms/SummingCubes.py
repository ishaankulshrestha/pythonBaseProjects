mydict = {}
mylist = []

for i in range(1,1001):
    for j in range(i+1,1001):
        num = i**3 + j**3
        if num in mydict.keys():
            #print(i,j,num)
            try:
                l = mydict[num]
                l.append((i,j))
                mydict[num] = l
            except Exception as e:
                print(" {} {} {} ".format(i,j,num))
                print(mydict)
                print(e)
            #print(mydict)
        else:
            mydict[num] = [(i,j)]

for mykeys in mydict.keys():
    if len(mydict[mykeys]) > 1:
        print(mydict[mykeys],end=" ")
        print("")

