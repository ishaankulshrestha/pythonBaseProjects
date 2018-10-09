import re

### Example 1
prog = re.compile(r'm\w\w')
str = "cat mat bat rat"
result = prog.search(str)
print(result.group())

## instead two lines in above code can be combined to perform below :
result = re.search(r'b\w\w',str)
print(result.group())

## 