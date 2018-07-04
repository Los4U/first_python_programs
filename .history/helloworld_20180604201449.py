import sys
person = []
counter = 1
while counter != len(sys.argv):    
    person.append(str(sys.argv[counter]))
    counter = counter + 1

def hiWorld():
    print("Hello world!")

def hiPersons():
    print("Hello ", end="")
    print(*person, sep=' & ')

if len(sys.argv) > 1:
    #show(sys.argv[1])
    hiPersons()
else:
    hiWorld()

