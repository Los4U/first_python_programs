import random

list = ["Kamil", "Szymon", "Basia", "Grzegorz", "Piotrek", "Karol" ]
#lenght = len(list)
print("Ilość osób: " + str(len(list)))

for i in range(6):
    random_person = list[random.randrange(0,len(list))]
    if i%2 == 0:
        print("Zespół:")
    print("  -" + random_person)
    list.remove(random_person)
    #lenght = len(list)