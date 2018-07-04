number = 1
i = 1
how_many=0
while True:
#for i in range(300):
    if number%7==0 and number%9==0:
        print(str(i) + ": " + number)
        how_many+=1
        i=+1

    number=number+1
            
    if how_many==25:
        print("lalalal")
        break