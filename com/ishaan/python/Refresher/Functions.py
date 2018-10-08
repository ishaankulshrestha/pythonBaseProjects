from functools import reduce
a = 10
b = 20

c = lambda x,y:x if x > y else y

print(c(a,b))

list1 = [x  for x in range(1,6,1)]
list2 = [x*x for x in list1]

print(list2)

prod = reduce(lambda x,y:x*y,list1)
print(prod)

list3 = list(map(lambda x:x*x*x,list1))

print(list3)

