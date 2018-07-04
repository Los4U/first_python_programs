import sys
def show(who):
    print("Hello " + who + "!")

if len(sys.argv) > 1:
    show(sys.argv[1])
    #print("Hello " + sys.argv[1] + "!")
else:
    print("Hello world")