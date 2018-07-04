import sys
def show(who):
    print("Hello " + who + "!")

if len(sys.argv) > 1:
    show(sys.argv[1])
else:
    show("world!")

for i in sys.argv:
    persons = person + i + "- "
    
print(persons)