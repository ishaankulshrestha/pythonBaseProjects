import math

test_case = int(input())

for _ in range(test_case):
    numbers = int(input())
    min = math.inf
    for k in range(numbers):
        current = int(input())
        if k == 0:
            prev = current
            continue
        if prev - current > 0 and prev - current < min:
            min = prev - current
        if prev - current < 0 and current - prev < min:
            min = current - prev
        if prev == current:
            min = 0
            break

