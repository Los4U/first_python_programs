number = 1
how_many=0
#while True:
for i in range(300):
    number=number+1
    if number%7==0 and number%9==0:
        print(number)
        how_many=+1

    if how_many==25:
    print("25") 
    #    break
   