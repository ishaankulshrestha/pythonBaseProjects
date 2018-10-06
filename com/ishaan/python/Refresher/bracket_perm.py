def perm(str1,str2,my_set):
    if str1 == "":
        print_str(str2,my_set)
    for i in range(len(str1)):
        perm(str1[:i]+str1[i+1:],str1[i]+str2,my_set)

def print_str(str2,my_set):
    stack = []
    for ch in str2:
        if ch == '{':
            stack.append('}')
        if ch == '}':
            if stack == [] or stack.pop() != '}':
                return
    if stack != []:
        return
    my_set.add(str2)

my_set = set()
perm("{{{{}}}}","",my_set)
print(my_set)