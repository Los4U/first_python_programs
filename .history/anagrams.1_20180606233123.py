import sys

file = open(str(sys.argv[1]), "r")
words = file.read().splitlines()

p2 = 1 
for word in words:
    for p2 in range (p2, len(cont)-1):
        if sorted(cont[word]) == sorted(cont[p2]):
            print(str(word) + ":" +  str(p2) + ":" + cont[p2])
            
file.close()    