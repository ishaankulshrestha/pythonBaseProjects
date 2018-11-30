from random import randint

# for i in range(1,31,1):
#     n = randint(70,150)
#     print("('2018-01-{}', {}),".format(i,n))

names = [chr(a)+chr(b) for a in range(65,65+11) for b in range(65,65+11) ]

for name in names :
    print("('{}','HIN',{}),".format(name,randint(10,100)))
    print("('{}','ENG',{}),".format(name, randint(10, 100)))
    print("('{}','MAT',{}),".format(name, randint(10, 100)))