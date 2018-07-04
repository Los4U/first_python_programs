import random
list = ["Kamil", "Szymon", "Basia", "Grzegorz", "Piotrek", "Karol" ]
list2 = list
print("Ilość osób: " + str(len(list)))
for i in range(3):
    random_person1 = list[random.randrange(0,len(list))]
    list.remove(random_person1)
    random_person2 = list[random.randrange(0,len(list))]
    list.remove(random_person2)
    print(" Zespół: "+ str(random_person1) + " & " + str(random_person2) )

print("\n")

print("Ilość osób: " + str(len(list2)))
for i in range(6):
    random_person = list2[random.randrange(0,len(list2))]
    if i%2 == 0:
        print("Zespół:")
    print("  -" + random_person)
    list2.remove(random_person)    