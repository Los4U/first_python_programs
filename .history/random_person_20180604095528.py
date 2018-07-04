import random

list = ["Kamil", "Szymon", "Basia", "Grzegorz", "Piotrek", "Karol" ]
lenght = len(list)
print("Ilość osób: " + str(lenght))

for i in range(6):
    random_person = random.randrange(1,5)
    print(random_person)

#random_person