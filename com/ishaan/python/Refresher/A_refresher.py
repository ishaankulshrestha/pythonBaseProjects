#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:55:24 2018

@author: ishaan
"""

a, b, c, d, e = 1, 2, 3, 4, "ishaan"
print(a, b, c, d, e)

list1 = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
print(list1)
print(list1[0:5])

tuple1 = (1, 2, 3, 4)
print(tuple1)
print(tuple1[2:4])

dictn = {"name": "ishaan", "company": "snapdeal", "desg": "ds"}
print(dictn.get("name"))

print(a + b)

print(b % c)

print(b ** c)

if (a < b and b < c):
    print("yes")
else:
    print("no")

if (not a > b and b < c):
    print("yes")
else:
    print("no")

if (3 in list1):
    print("it is there")
else:
    print("it is not there")
a = 1
while (a < 10):
    a = a + 1
    if (a == 3):
        continue
    print(a)
    if (a > 4):
        break

for i in range(20):
    print(i)
for i in list1:
    print(i)
for i in range(5):
    for j in range(5):
        print(i * j)

it = iter(list1)
nx = next(it)
print(nx)


## GENERATOR FUNCTION

def add1(n):  # generator function
    sum = 0
    for i in range(n):
        sum = sum + i
        yield sum


f = add1(20)  # f is iterator object

for i in range(10):
    print(next(f))

import math

print(math.pi)
print(math.e)

var1 = 'Hello World!'
var2 = "Python Programming"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

var1 = 'Hello World!'
print("Updated String :- ", var1[:6] + 'Python')

print('a' * 10)

print("let us see %s how this format %10d and %20d" % ("ishaan", 7, 6))

## use """ for multiline operations


#### Lists

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list1[3] = 2001

del list1[2]

print(list1)

## Tuples

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

### Tuple and List Operattion
## cmp, len , max, min, tuple

di = {"key1": 10, "key2": 20, "key3": 30}
print(di["key1"], "Hi", di.get("key2"))
print(di)

for i in di.keys():
    print(di.get(i))

keys = iter(di)
for i in keys:
    print(i)


def addme(a, b=2):
    return a + b * 2


print(addme(8))


### All parameters (arguments) in the Python language are passed by reference.

# Variable Function definition is here
def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50)

### Scope Global and local both


# When you import a module, the Python interpreter searches for the module in the following sequences −
#
# The current directory.
#
# If the module is not found, Python then searches each directory in the shell variable PYTHONPATH.
#
# If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python3/.


# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)

# Close opened file
fo.close()

# import os
# os.rename(f1,f2)
# os.remove("hi.txt")
os.mkdir("test")
os.chdir("newdir")
os.getcwd()






