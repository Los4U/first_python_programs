import random

list = ["Kamil", "Szymon", "Basia", "Grzegorz", "Piotrek", "Karol" ]
lenght = len(list)
print("Ilość osób: " + str(lenght))

for i in range(lenght):
    random_person = list[random.randrange(1,lenght)]
    print(random_person)
    list.remove(random_person)
    lenght = len(list)