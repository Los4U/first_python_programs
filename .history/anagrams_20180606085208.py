import sys
from os import path


for i in sys.argv[1:]:
    print(i)
    file = open(i, "r")
    cont = file.read().splitlines()
    print(cont)
    for lin in len(cont):
        print(lin)
    file.close