import sys

file = open(str(sys.argv[1]), "r")
words = file.read().splitlines()

p2 = 1 
for word in words:
    #print(sorted(word))
    i = 0
    for i in range(i, len(words)):
        if sorted(word) == sorted(words[i]):
            #print(i)
            print(i + ": " + word + " - " + words[i])
            i = i + 1
    #for p2 in range (p2, len(words)-1):
    #    if sorted(str(word) == sorted(word[p2])):
    #       print(str(word) + ":" +  str(p2) + ":" + word[p2])
            
file.close()    