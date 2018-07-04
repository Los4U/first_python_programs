import sys
from os import path


#for i in sys.argv[1:]:
#print(i)
file = open("anagrams.csv", "r")
cont = file.read().splitlines()
#print(cont)
p1 = 0
p2 = 1 
for b in range(0,len(cont)):

    for c in range (p2, len(cont)):

        if sorted(cont[b]) == sorted(cont[p2]):
            print(str(b) + ":" + cont[b] + " = " +  str(p2) + ":" + cont[p2])
            
        #p2 = p2 + 1
    #b = b + 1
file.close()    