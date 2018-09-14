def getpos(lst,x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    print("returning -1")
    return -1


files = open("/home/ishaan/Desktop/source.txt",mode='r')
dict1 = dict()
word =[]
freq = []
for i in files:
    for j in i.split(" "):
        #print(j)
        j = j.lower()
        if j.isalnum():
            dict1[j] = dict1.get(j,0) + 1
            if(len(freq) < 10):
                word.append(j)
                freq.append(dict1[j])
            elif j in word :
                pos = getpos(word,j)
                freq[pos] = dict1[j]
            elif dict1[j] > min(freq):
                pos = getpos(freq,min(freq))
                freq[pos] = dict1[j]
                word[pos] = j

#print(" {} \n {}".format(word,freq))

answer = dict(zip(freq,word))

for i in sorted(answer.keys(),reverse=True):
    print(" Word '{}' have frequency -- {}".format(answer[i],i))


print(answer)

