import sys

file = open(str(sys.argv[1]), "r")
words = file.read().splitlines()

p2 = 1 
for word in words:
    #print(words.index(word))
    i = 0
    for i in range(i, len(words)):
        if sorted(word) == sorted(words[i]):
            if words.index(word) != i:
                #print(words.index(word))
                #print(i)
                print(str(words.index(word)) + ": " + word + " - " + str(i) + ": "+ words[i])
            i = i + 1
file.close()    