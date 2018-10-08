l, b = (int(x) for x in input("Enter the length and breadth of rectangle seperated by comma \n").split(","))
print("\n\n")
for i in range(l):
    if i == 0 or i == l - 1:
        print('*' * b)
        continue
    print('*' + " " * (b - 2) + '*')

