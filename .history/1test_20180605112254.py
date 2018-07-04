import sys

words = []
words = sys.argv

for i in words:
    if i.endswith("e"):
        i = i[:-1]   #].remove[-1]
        i =  str(i) + "ing" #st[:-1]
        print(i)