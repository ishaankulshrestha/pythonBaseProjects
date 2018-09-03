filer = open("/home/ishaan/Desktop/checkmeout.txt",'r')
count = 0
for strngs in filer:
    count += 1
    print(str(count) + " " +strngs)
filer.close()

filew = open("/home/ishaan/Desktop/checkmeout.txt",'a')
for nums in range(10):
    filew.write(" adding line number {:10}\n".format(nums))
filew.close()

