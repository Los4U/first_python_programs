import sys

words = []
words = sys.argv
exception = ["be", "see", "flee", "knee", "etc" ]
for i in words:
    if  i in exception  :                       #i.endswith("e"):
        i = i[:-1]   #].remove[-1]
        i =  str(i) + "ing" #st[:-1]
        print(i)