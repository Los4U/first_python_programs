import sys
name = sys.argv
if len(name) > 1:
    print("Hello " + name[1])
else:
    print("Hello world")