from collections import deque

myDeque = deque()

for i in range(1,11):
    if i%2 == 0:
        myDeque.appendleft(i)
    else:
        myDeque.append(i)

print(myDeque)

for i in range(1,11):
    if i%2 != 0:
        print(myDeque.popleft())
    else:
        print(myDeque.pop())