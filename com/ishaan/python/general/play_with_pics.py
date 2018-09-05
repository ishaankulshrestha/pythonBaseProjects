files = open("/home/ishaan/Desktop/sizes.csv","r")
tables = []
counter=0
for i in files:
    counter += 1
    lines = list(i.split("|"))
    lines[2] = int(lines[2][:(len(lines[2])-1)])
    tables.append(lines)
    #if counter > 1000:
        #break
files.close()
databases = dict()
for names in list(tables):
    #print(names)
    databases[names[0]] = databases.get(names[0], 0) + 1
for names in databases.keys():
    print("{} has {} tables".format(names, databases[names]))


