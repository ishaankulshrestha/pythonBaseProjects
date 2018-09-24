def fib(n,my_dict):
    if n <= 0 :
        return 0
    if n == 1 :
        return 1
    if n in my_dict:
        #print("already know value for {} is {}".format(n,my_dict[n]))
        return my_dict[n]
    result = fib(n-1,my_dict) + fib(n-2,my_dict)
    my_dict[n] = result
    return  result
my_dict = dict()
for i in range (0, 21):
    print(fib(i,my_dict),end=" ")


