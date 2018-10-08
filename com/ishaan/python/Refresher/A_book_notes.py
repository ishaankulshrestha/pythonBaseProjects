def dis(str):
    print("\n" + '*' * 20 + " " + str + " " + '*' * 20+"\n")


dis("Comments")

## This is a single line comment
""" This can be used as a multiline comment or actually docstring """

dis("None as Null in java")

a = None
if a is None:
    print("A is none")
else:
    print("A is not none")


dis("Type Conversion ")

print(type("1234"))
b = float("1234")
c = int("1234")
print(type(b))

num = 1234
strs = str(1234)
print("strs is {} type".format(type(strs)))


dis("Base conversion ")

a = int("1010",2)
print("1010 in int is {} \n".format(a))

a = bin(100)
b = hex(100)
c = oct(100)

print("bin , hex and oct for 100 is {} , {}  and {} ".format(a,b,c))


dis("True ( T capital)  for true and False (F capital) for false")

if -9:
    print("-9 is True ")
else:
    print("-9 is False")

if 0:
    print("0 is True ")
else:
    print("0 is False")

dis("Seq data type are str,bytes,bytearray,list,tuple,range. Can be Slice,dice and multiply")

str = "Ishaan"
str_rev = str[::-1]
str_start = str[:len(str)//2]
print("Reverse string is {} and first half is {} 4 times is {}".format(str_rev,str_start,str*4))

dis("bytes and bytearrys .. check use below TODO")

dis("List are like arrays except : a) they can store hetro data b) they can grow dynamically.")

my_list = []

inc =3
for i in range(100,200,inc):
    my_list.append(i)
    inc += 1
print(my_list)

my_list.append(1)
my_list.pop()
my_list.remove(my_list[10])
print(my_list.count(1))
my_list.extend([1,2,3])
my_list.reverse()
print(my_list.pop(0))


dis("tuple are like lists which can not be modified and they can have Duplicates.")





