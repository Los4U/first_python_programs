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
    person.append(str(sys.argv[counter]))
    counter = counter + 1

#print(person)

#mylist = ["x", 3, "b"]
#    for items in person:
#       print(items)

print(*person, sep=', ')