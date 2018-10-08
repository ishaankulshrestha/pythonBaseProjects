from random import randint
my_list = []
for i in range(10):
    sub_list = [randint(1,1000),randint(1,1000),randint(1,1000)]
    my_list.append(sub_list)

for ele in my_list:
    print(ele)

### Note the following 2 statements

new_list = sorted(my_list,key=lambda x:x[1])
my_list.sort(key=lambda x:x[1],reverse=True)

print("Sorted Values are as follows : ")

for ele in new_list:
    print(ele)

print("Sorted Values are as follows : ")

for ele in my_list:
    print(ele)