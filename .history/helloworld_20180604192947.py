import sys
def show(who):
    print("Hello " + who + "!")

if len(sys.argv) > 1:
    show(sys.argv[1])
else:
    show("world!")

person = []
#for i in sys.argv:
#    persons = person + i

counter = 1
while counter != len(sys.argv):    
    person.append(sys.argv[counter])
    counter= counter + 1

print(persons)