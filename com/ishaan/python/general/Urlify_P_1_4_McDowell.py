## Following program is to replace " " with "%20" as done in urls
## Efficiently done in (n) and space as well O(1). i.e. without using extra space.

strs = "Hello there I am iks"
lst = list(strs)
k = len(lst)
#   print(lst)
counts = 0
for ch in strs:
    if ch == " ":
        counts += 1

for i in range(k,k + counts*2):
    lst.append(".")
print(lst)
index = k + counts*2
for i in range(k-1,0,-1):
    if(lst[i] == " "):
        lst[index-1] = "0"
        lst[index-2] = "2"
        lst[index-3] = "%"
        index -= 3
    else:
        lst[index-1] = lst[i]
        index -= 1

print("".join(lst))