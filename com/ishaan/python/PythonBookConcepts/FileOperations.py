from random import randint
f = open("/home/ishaan/Desktop/sample.txt","w")
for i in range(100):
    no_words = randint(10,20)
    curr_sen = ""
    for j in range(no_words):
        word_len = randint(5,15)
        currword =""
        for k in range(word_len):
            ch = randint(65+32,65+32+25)
            currword = currword+chr(ch)
        curr_sen = curr_sen +" " + currword
    f.write(curr_sen)
    f.write("\n\n")
f.close()

f_read = open("/home/ishaan/Desktop/sample.txt","r")

count = 0

for line in f_read:
    for word in line.split(" "):
        count += 1
        print(count,end="  ")
        print(word)

f_read.close()


