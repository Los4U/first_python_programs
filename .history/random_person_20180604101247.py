import random

list = ["Kamil", "Szymon", "Basia", "Grzegorz", "Piotrek", "Karol" ]
lenght = len(list)
print("Ilość osób: " + str(lenght))

for i in range(6):
    random_person = list[random.randrange(0,lenght)]
    if i%2 == 0:
        print("Zespół:")

    print(random_person)
    list.remove(random_person)
    lenght = len(list)