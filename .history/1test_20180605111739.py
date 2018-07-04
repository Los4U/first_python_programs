import sys

words = []
words = sys.argv

for i in words:
    if i.endswith("e"):
        i.remove[-1]
    
    print(i)