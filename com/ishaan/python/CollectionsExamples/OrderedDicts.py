from collections import OrderedDict
from random import randint

mydict = OrderedDict()
mydict1 = dict()

for i in range(1,31,1):
    n = randint(1,101)
    mydict[i] = i*2
    mydict1[i] = i*2

# for i in range(2,31,3):
#     n = randint(1,101)
#     mydict[i] = i*2
#     mydict1[i] = i*2
#
# for i in range(3,31,3):
#     n = randint(1,101)
#     mydict[i] = i*2
#     mydict1[i] = i*2

for k,v in mydict.items():
    print(" for key {} value is {} ".format(k,v))

for k,v in mydict1.items():
    print(" for key {} value is {} ".format(k,v))

#print(mydict1)


