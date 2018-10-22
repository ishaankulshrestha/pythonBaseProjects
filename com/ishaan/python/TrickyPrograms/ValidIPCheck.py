def ifvalidIP(ip):
    my_list = ip.split(".")
    if len(my_list) != 4:
        return False
    for ele in my_list:
        if not ele.isdigit():
            return False
        if not (0 <= int(ele) <= 255):
            return False
    return True

print(ifvalidIP("23.44.56.254"))
print(ifvalidIP("23.44.56.25K"))
print(ifvalidIP("-1.44.56.254"))
print(ifvalidIP("23.44.56.258"))