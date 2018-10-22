def wordLength(sentence):
    wordscount = charac = 0
    for word in sentence.split(" "):
        if word == "":
            continue
        wordscount += 1
        charac += len(word)
    return charac*1.0/wordscount

print(wordLength(" hello dear how are   you! "))
