import sys
person = []
counter = 1
while counter != len(sys.argv):    
    person.append(str(sys.argv[counter]))
    counter = counter + 1

def hiWorld():
    print("Hello world!")

def hiPerson(name):
    print("Hello " + name + "!")

def hiPersons():
    print("Hello ", end="")
    print(person[1],person[2], sep=' & ')

if len(sys.argv) == 2:
    hiPerson(sys.argv[1])
elif len(sys.argv) > 2:
    hiPersons()
else:
    hiWorld()

