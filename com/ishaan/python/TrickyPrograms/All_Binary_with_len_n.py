def binstrs(num):
    if num == 0:
        return []
    if num == 1:
        return ['0','1']
    return(digit+bitstring for digit in ['0','1'] for bitstring in binstrs(num -1))

print("Hi this is {}".format(binstrs(4)))

### Not working Some How ###


