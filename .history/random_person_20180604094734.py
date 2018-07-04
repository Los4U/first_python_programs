import random
list = ["Kamil", "Szymon", "Basia", "Grzegorz", "Piotrek", "Karol" ]
lenght = len(list)
print(lenght)

for i in list:
    random_person = random.randrange(1,lenght)
    print(random_person)



