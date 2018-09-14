str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = []


def getcomplength(str1):
    i=0
    length = 0
    while i < len(str1):
        while i+1 < len(str1) and str1[i] == str1[i+1] :
            i += 1
        length += 2
        i+=1
    return length


i=0
while i < len(str1):
    str2.append(str1[i])
    count=1
    while i+1 < len(str1) and str1[i] == str1[i+1] :
        count += 1
        i += 1
    str2.append(str(count))
    i += 1
print(str1)
print("".join(str2))
print("length of string above is {}".format(len(str2)))
print("Length of compressed string will be {}".format(getcomplength(str1)))

