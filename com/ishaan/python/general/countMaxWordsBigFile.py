
file = open("/home/ishaan/Desktop/m/Archive20170426/big.txt",mode="r")

i = 0
my_dict = dict()

for line in file:
    for words in line.split(" "):
        if not words.isalnum():
            continue
        i+= 1
        #print(i,words)
        my_dict[words.lower()]  = my_dict.get(words.lower(),0) + 1
i=0

real_dict = dict()

for key,value in my_dict.items():
    real_dict[value] = real_dict.get(value," ")+key+" "

my_keys = sorted(real_dict.keys())

for key in my_keys:
    print(key,real_dict[key])

file.close()

