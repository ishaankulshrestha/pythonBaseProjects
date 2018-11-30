def get_subset(old,new):
    if check(new):
        print(new)
    else :
        return
    for i in range(len(old)):
        get_subset(old[:i]+old[i+1:],old[i] + new)


def check(new):
    old = None
    for ch in new:
        if old is None :
            old = ch
            continue
        if old > ch:
            return False
        old = ch
    return True

get_subset("1234","")

