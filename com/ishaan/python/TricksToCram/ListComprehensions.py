my_list = list()
for i in range(1,11):
    my_list.append(i)


sqr = [x**2 for x in my_list]
print(sqr)


evn_sqr = [x**2 for x in my_list if x%2 == 0]
print(evn_sqr)

sum = [x + y for x in range(1,10,2) for y in range]

