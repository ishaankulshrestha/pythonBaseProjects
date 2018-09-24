lst = [0,1,1]

## solving for complexity O(n)

for i in range(3,21):
    lst.append(lst[i-1]  + lst[i-2])
for i in lst:
    print(i,end =  " ")