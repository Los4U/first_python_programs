import sys

file = open(str(sys.argv[1]), "r")
cont = file.read().splitlines()

p2 = 1 
for b in range(0,len(cont)):
    for p2 in range (p2, len(cont)-1):
        if sorted(cont[b]) == sorted(cont[p2]):
            print(str(b) + ":" + cont[b] + " = " +  str(p2) + ":" + cont[p2])
            
file.close()    