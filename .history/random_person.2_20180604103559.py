import random
list = ["Kamil", "Szymon", "Basia", "Grzegorz", "Piotrek", "Karol" ]
print("Ilość osób: " + str(len(list)))

for i in range(3):
    random_person1 = list[random.randrange(0,len(list))]
    list.remove(random_person1)
    random_person2 = list[random.randrange(0,len(list))]
    list.remove(random_person2)
    print("Zespół: "+ str(random_person1) + " & " str(random_person2) )
    #if i%2 == 0:
        
    #print("  -" + random_person)
    #list.remove(random_person)