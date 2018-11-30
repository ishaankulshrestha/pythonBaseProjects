import heapq
my_file = open("/home/ishaan/Desktop/sample.txt","r")

my_dict = dict()
freq_words = dict()

for line in my_file:
    for word in line.split():
        print(word)
        if word.isalnum():
            my_dict[word] = my_dict.get(word,0) + 1
            if len(freq_words) < 10 :
                freq_words[word] = my_dict.get(word,0)
            else:
                if word in freq_words:
                    freq_words[word] = my_dict.get(word,0)
                if min(my_dict.values()) < my_dict.get(word,0):
                    pass

            freq_words.append((my_dict[word],))









my_file.close()