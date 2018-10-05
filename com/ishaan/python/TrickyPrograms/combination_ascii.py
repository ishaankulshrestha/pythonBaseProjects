def getsum(num):
    if num is None:
        return 0
    sum = 0
    for digits in num:
        sum += digits
    return sum


def get_comb(my_str, num):
    #print("Value of num is {} and sum is {}".format(num,getsum(num)))
    if num is None:
        num = []
    if getsum(num) > len(my_str):
        return
    if getsum(num) == len(my_str):
        #print("Value of num is {}".format(num))
        func_print(my_str, num)
        return
    num1 = num[:]
    num2 = num[:]
    num1.append(1)
    num2.append(2)
    get_comb(my_str, num1)
    get_comb(my_str, num2)


def func_print(my_str, num):
    frm = 0
    for i in num:
        if int(my_str[frm:frm + i:1]) > 26:
            return
        frm += i
    frm = 0
    for i in num:
        print(chr(ord('a') + int(my_str[frm:frm + i:1]) - 1), end="")
        frm += i
    print("")


get_comb("123123", list())
