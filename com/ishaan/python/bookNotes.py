Py BK Nts

>> to get pyc of python -- "python -m py_compile x.py" -- supply pyc like we do for jar.
>> gc have collect() method for garbage collection.
>> #single line comment """ or ''' ( docstring) for multiline

DATATYPES

>> None in python is like null of Java 
>> Numeric types are int,float,files : converted with int(),float() and complex() func.
>>  int(str,base) this will convert from given base to decimal number. i.e. 110 >> 6xN
>> bin(),oct(),hex() are  functions for decimal to given base conversion i.e. 6 >> 110
>> True and False >> False is 0 or empty .. rest every thing is considered as true.
>> Sequence datatype -- str,bytes,bytearray,list,tuple,range
>> String >> str[k],str[k:l],str[k:],str[:k],str[-1] also str*2 all works
>>bytes and bytearray ?? check use
>> List are like arrays except : a) they can store hetro data b) they can grow dynamically.
>> tuple are like lists which can not be modified and they can have Duplicates.
>> slice and dice are applicable to list and tuples.
>> range(start,end,step) -- end (upper bound) excluded and default end is INF step is 1
>> [ ] for lists, { } for sets , ( ) for tuples, { key:val } - Dictionaries , 
>> Default is always tuples i.e. var = 1,2,3,4 will make var a tuple
>> set and dict are un-ordered because they are generate with hash
>>  immutable data types are tuples , int,float,complex, str, frozenset
>>  slice and dice is not applicable to set and dict ( since no order is there)
>>  set.update() - to add : set.remove() :to remove. -- will not work on frozenset.
>> dict { key1:val1,key2:val2}
>> d.keys() and d.values() will give list of keys and values.
>> \ is esc character and type(var) will give type of a variable.
>> Every data type in python is treated as class and its variables as object.
>> No char type in Python. char are string of length 1
>> str[0].isupper() is a function.
>> No constant provision in python though same are denoted by CAPS.
>> Python is case sensitive
>> Conventions in python >> word should separate by _
>> non public instance variable should start with _
>> non accessible entities should stat and end with __
>> instance methods should have first arg is "self" and class methods "cls"

OPERATORS 

>> / will give float result
>> // will give quotient only ( i.e. the whole part of answer ignore decimal)
>> % gives reminder  and ** give power.
>> x += val work for all  operators
>> a=b=c=d=1 :: a=1;b=2:: a,b,c,d = 1,2,3,4  .. all these will work 
>> 10<x>20>15<13 will work
>> False indicates 0 & True any other number 
>> 2 and 1 == 2 :: 2 or 1 == 1 :: 
>> Bitwise operator ~,&,|,^,<<,>>
>>  x in strings,lists,tuples or dictionaries ( and "not in" as well)
>> for city in dict means for city in dict.keys()
>>  for key,value in dict1.items()
>>  "obj1 == obj2" this will check values
>> "obj1 is obj2" will check identity ( memory i.e. same id or not )   
>> import math VS from math import sqrt :: later will save resources
>> const in math pi,e,inf & nam e

INPUT OUTPUT 

>> print("hi"*3 + "world") >> hihihiworld  ALSO , can be used against + but will give space
>>  print("{:8} is greater than {}".format(a,b), sep = "|" , end = "\t") :: use this always 
>> :8 in above will give spacing of 8
>>  str = list(input("Enter the string number {}".format(num)).split("|") )
>> str[3] = int(str[3])
>> a,b,c = input("Enter any three numbers").split(" ")  :: works very well *****
>> ALSO a,b,c = [int(x) for x in input("Enter 3 numbers").split(" ")] *****
>> x = eval(input("Enter any expression")) :: input value will work as command ****
>> sys.argv is list containing  command line argument -> args = sys.argv then args[0] will tell program name and rest args[1],args[2] will tell passed arguments
>> use argparse module to make standard program which will help users to know how to use arguments 

>> CONTROL STATEMENTS

>> if .. elif .. elif .. else (else is not compulsory)
>> while condition :
>> for ch in string1 :: range(1,10,2) :: list::tuple::dict::dict.keys()::dict.values
>> inifinite , nested loop
>> for else suite : else is always executed if break is not encountered.
>> break,continue and pass( do nothing) are flow statements
>> assert condition , message .. this will raise exception if condition is not matched.
>>return statement (s)

STRING AND CHARACTERS

>> No Separate char type .. char are string of size 1 
>> str1 = "bla" or 'bla' or """bla""" :: last being multi line
>> raw string by adding r"hello\nji" and u"HelloBuddy" for unicode 
>> \n will not be treated as new line in raw
>> len(str) for length, str[-1]  for last character
>> we can also do print(str[3,40,2] -> start,stop and stepsize
>> for i in str1[ : : -1]:  print(i,end=" ")  -> shorted way to reverse string.
>>   print(str*10) -> this will print str 10 time
>> str.strip() will remove spaces, lstrip,rstrip is there
>> strings can be compared with > < == etc 
>> str.find(substring,beg,end) -> will give first occurance
>> str.count(substr) or str.count(substr,beg,end)
>> Strings are immutable which gave same Performance and Security
>> S1 = S2 means S1 and S2 are pointing to same memory address which S2 was pointing to 
>> str.replace(sub1,sub2) :: to replace in string
>> str.split(",") will give a list of words separated by ","
>> strnew = "-".join(seq) seq can be list,tuple etc
>> str.upper(), lower(), swapcase(),title()
>> str.startswith(substr) , str.endswith(substr) will give True or False
>> isalnum(),isalpha,isdigit(),islower(),isupper(),istitle(),isspace()
>> Formatting "hello {} , you are {} years old.".format{name,age}
>> { : } >> s-> string::f->float::d->decimal:: c->character:: x,o,b for hexa,octa and bin
>>{ :15d} or {:*>15d} or {:*^15d}
>> # in format to express hexa,octa,binn with prefix
>> str.sort() will sort the str and save while sorted(str) will return a new string keeping str same.
>> sorted works on list as well 
>> len(str) -> length 
>> to insert substring in a string use join along with lists
 

FUNCTIONS :

>>  Function gives reuse,modular,maintenance,debug,reduce length
>> A function inside a class is know as method
>> def(a,b) : <Body in next line with return in end if applicable>
>> dynamic typing :: types of parameter are recognized at run time.
>> return a , b, c is valid .. this will be passed as tuple.
>> Python treats only 0 as False rest every thing is True
>> Function are object and can be passed like object 
>> Its possible a function to be passed to other function and returned as well.
>> Its possible to assign a function to a variable and write nested function
>> objects are stored in heap memory
>> immutable are passed by value and mutable are passed by reference
>> formal argument are variable and actual arguments are values passed
>> def sum(a,b=10): for default of b if not passed
>> while calling we can call like sum(b=9,a=10) so order wont matter
>> def add(farg,*args) for variable length :: farg will contain length and args is list of args
>> use global keyword for having global scope
>> global function is also used
>> lst = [int(x) for x in input.split(",")) *****
>> Lambda function -> f = lambda x:x*x
>> max  = lambda x,y:x if x>y else y
>> filter() with lambda :: filter(is_even,list) will return list
>> lst1 = list(filter(lambda x: x%2==0),lst) ******
>> map(function,sequence) 
>> lst1 = list(map(lambda x: x*x,lst)) ******
>> prod = reduce(lambda x,y : x*y,lst)****** it will give the product of all elements
>> reduce needs to be imported by functools
>> Decorators are function which accepts and returns a function
>> Generators are function to returns seq of values using yield 

def demo():
    for i in range(100,10000,100):
        yield i


g = demo()
for _ in range(10):
    print(next(g))

>> module is importable code
>> if __name__ != '__main__' then program is called form somewhere else as module


LISTS 

>> Arrays vs List :: hetro and homo :: fixed and dynamic
>> list = [] for empty list
>> seq operation are applicable lst[2,20,2] :: len(lst) :: lst1+lst2 :: lst1*10 :: x in lst1 :: for i in lst1
>> lst = list[range[1,100,2]
>> lst.append(), del lst[1],lst.reverse(),
>> lst1 = lst2 will make both list to point to same memory address
>> to clone we should us lst1 = lst2[:] OR lst1=lst2.copy()
>> List Methods :: index(x), append(x), insert(i,x), list.copy(), extend(lst1), count(x), remove(x), pop(x), sort(reverse = True),reverse(), clear(), min(), max()
>> st1 = set(list) .. and set1.intersection(set2)
>> Nested list can be used as arrays or matrices 
>> List comprehension *******
          sqr = [x**2 for x in range(1,11) if x%2 == 0]
           lst = [i+j for i in x for j in y]
           lst = [w[0] for w in words]
          lst = [i for i in num1 if i not in num2]

sorted(my_list) will use TimSort. Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data

comparator >> data = sorted(data, cmp=Students.comparator)
where data is list of type class Student

TUPLES
>> tuples are similar to list except they are immutable
>> tup1 = () or tup =(10,) :: not , for a single element in tuple is mandatory
>> x = 1,2,3,4,5 :: x will be a tuple by default
>> like list() function we have tuple() and set() function as well
>> mostly all function of list applicable here except changing one
>> str.split() will give list and x = 1,2,3 will give tuple
>> Nested tuples also there like nested list
>> sorted(tup1,key=lambda x:x[1]) to sort nested tuple *****
>> tuples being immutable are appended, inserted and deleted by "+" and slicing function

DICTIONARIES : 

>> dict1 = {"key1":"value1","key2","value2"} :: key can be immutable type i.e. int,str,tuple etc
>> dict1["key1"] is allowed but no slicing is allowed i.e. dict[0:5] is invalid
>> len[dict1] will give the number of keys ( or pairs)
>> dict are not ordered as they come from HASH operation 
>> del dict[key], dept in dict are valid. Keys will be searched in later case.
>> Keys are unique is tried to enter twice .. later will be the value.
>> Methods :: d.clear(), d1 = d.copy(), d.fromkeys(s[,v]), d.get(k[,v]), d.items(), d.keys(), d.values(), d.update(x), d.pop[k[,v]), d.setdefault[k[,v])
>> eval() is also important as input may be provided as dictionaries
>> sum(dict.values) will work 
>> x.update({k:v}) will work
>> x['key'] may give error .. try using x.get(key,default) 
>> for k in dict.. will loop on keys 
>> dict.keys() and dict.values() are quite popular
>> for k,v in dict.items() *****
>> dict[x] = dict.get(x,0) + 1 is most used *****
>> sorted(dict.items,key= lambda t:t[1]) ******
>> List to Dictionaries :: z = zip[countries,cities] :: dict1 = dict(z)
>> String to Dict :: jst keep splitting and use common sense :: 


EXCEPTIONS:

try:
    statements
except ValueError:
    handler1
except ZeroDivsionError:
    handler2
except:
     handler3 #This will catch any left out generic exception
else:
     statements #When no exception is raised
finally:
     statements #Every time where any or no exception is raised.

CHARACTER ENCODING:

ASCII defines 128 characters, which map to the numbers 0–127. Unicode defines (less than) 221 characters, which, similarly, map to numbers 0–221 (though not all numbers are currently assigned, and some are reserved).

Unicode is a superset of ASCII, and the numbers 0–128 have the same meaning in ASCII as they have in Unicode. For example, the number 65 means "Latin capital 'A'".

Because Unicode characters don't generally fit into one 8-bit byte, there are numerous ways of storing Unicode characters in byte sequences, such as UTF-32 and UTF-8.

https://stackoverflow.com/questions/19212306/whats-the-difference-between-ascii-and-unicode


print(int("914",16))
print(chr(int("914",16))) give औ


REGULAR EXPRESSION IN PYTHON

>>import re 
>>we use raw string in regex which is denote by prefix "r" in any string
>> prog = re.compile(r'm\w\w') ; result = prog.search(str); print(result.group)
>>searh will search first occurance only
>> use findall to find all it will return a list of matched strings
>> result = findall(r'm\w\w',strs)
>> \w is for alpha and numbers \W is for reverse
>> re.match  will match from begining
>> re.split will split the string . re.split(r'\W+',strs) will seperate alphanum
>> re.sub(regex,newstr,str) will replace all regex matches with newstr
>> + mean 1 or more character
>> So all function -- match,search,findall,split,sub()
>> \d for digit \D for reverse
>> \s for white space \S for not white space
>> \w for alphanum \W for opp
>> \b space around word
>> \A matches starting of string
>> \Z matches end of string
>> + for 1 or more
>> * for 0 or more
>> ? for 0 or 1
>> {m} exact m 
>> { m,n} between m to n with default m to 0 and n to infinity
>> \ esc character 
>> . matches any char except new line
>> ^ matches beginning of string
>> $ matches end of string
>> more ... boring add later





(




GENERAL 

Math

>> Infinity in Math is "math.inf"

Sorting important for multiple arrays : 
contests = sorted(contests,key=lambda x:-x[0])
where contest = 2D or 3D array


__contains__(self)  defines in functionality 
__iter__(self) defines for in type (iterable) functionality 
__str__(self) defines print facility 

Bits operations: 
In python to convert into unsigned number just add 2**32

Heapq:

import heapq
heapq.heapify(my_list)
heapq.heappush(my_list,ele)
heapq.heappop(my_list)
heapq.nlargest(n,my_list)
heapq.nlargest(n,my_list)
 
 
#  GENERATE all sub sequence USE following EXCELLENT:
nums = [0,1,2]
bit_holder = [[]]

for i in nums:
            bit_holder +=[x + [i] for x in bit_holder]

print(bit_holder)
 
 
 
 
 
 
 
 
