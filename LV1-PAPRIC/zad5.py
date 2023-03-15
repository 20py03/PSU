with open ('song.txt','r') as filedata:
    dict={}
    for line in filedata:
        words=line.rstrip().split()
        for word in words:
            if word not in dict:
                dict[word]=1
            else:
                dict[word]+=1

print(dict)


        

