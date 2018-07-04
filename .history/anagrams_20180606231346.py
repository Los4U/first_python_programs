import sys
from os import path

file = open("anagrams.csv", "r")
cont = file.read().splitlines()

p1 = 0
p2 = 0 
for b in range(0,len(cont)):
    for p2 in range (p2, len(cont)):
        if sorted(cont[b]) == sorted(cont[p2]):
            print(str(b) + ":" + cont[b] + " = " +  str(p2) + ":" + cont[p2])
            
file.close()    