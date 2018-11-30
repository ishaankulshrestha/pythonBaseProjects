def perm(name1,name2):
    if name1 == "":
        print(name2)
        return
    for i in range(len(name1)):
        perm(name1[:i]+name1[i+1:],name1[i] + name2)

perm("ABCDEFG","")