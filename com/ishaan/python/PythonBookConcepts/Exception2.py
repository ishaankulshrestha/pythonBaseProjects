my_list = list(range(1,11))
print(my_list)

try:
    for i in range(11):
        print(my_list[i])
except:
    print("Exception is being raised at i = {} with exception {}".format(i))
finally:
    print("executing finally")

