import sys

words = []
words = sys.argv
exception = ["be", "see", "flee", "knee", "etc" ]
for i in words:
    if   i.endswith("e") and not i in exception:
        i = i[:-1]   #].remove[-1]
        i =  str(i) + "ing" #st[:-1]
        print(i)