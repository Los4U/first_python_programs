import sys
def show(who):
    print("Hello " + who + "!")

person = []
counter = 1
while counter != len(sys.argv):    
    person.append(str(sys.argv[counter]))
    counter = counter + 1

if len(sys.argv) > 1:
    show(sys.argv[1])
else:
    show("world!")

print("Hello" + *person, sep=', ')