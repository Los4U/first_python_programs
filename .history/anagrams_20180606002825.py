import sys
from os import path


for i in sys.argv[1:]:
    print(i)
    file = open(i, "w")