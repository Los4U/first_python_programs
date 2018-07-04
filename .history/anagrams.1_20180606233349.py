import sys

file = open(str(sys.argv[1]), "r")
words = file.read().splitlines()

p2 = 1 
for word in words:
    for p2 in range (p2, len(words)-1):
        if sorted(str(word) == sorted(word[p2])):
            print(str(word) + ":" +  str(p2) + ":" + word[p2])
            
file.close()    