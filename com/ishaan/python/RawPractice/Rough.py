def sample(x):
    x[0] *= 2
    print("In function x = {} ".format(x[0]))


x = (4,)
print("before call x = {}".format(x))
sample(x)
print("after call it is {}".format(x))
