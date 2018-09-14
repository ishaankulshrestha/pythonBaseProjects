mylist_1 = [2,9,8,9,9,9]
mylist_2 = [8,7,9,8,8,7]
third = []
carry = 0

if len(mylist_1) > len(mylist_2):
    first = mylist_1
    second = mylist_2
else:
    second = mylist_1
    first = mylist_2

for i in range(len(first)):
    if(i<len(second)) :
        third.append((first[i]+second[i] + carry)%10)
        carry = (first[i]+second[i] + carry)//10
    if(i>=len(second) and i < len(first)):
        third.append((first[i] + carry)%10)
        carry //= 10

while(carry > 0):
    third.append((carry) % 10)
    carry = carry//10

print(third)


