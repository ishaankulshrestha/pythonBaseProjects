# generate 100 no. - and find which are above 90 percentile

lst = []

for i in range(1,1001):
    lst.append(i*2)

sorted(lst)

print(lst)

n = len(lst)*(100-99)/100

print(n)

j=0

for i in lst[::-1]:
    if j > n:
        break
    j+= 1
    print(i,end=" ")


