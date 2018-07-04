number = 100
i = 1
how_many=0
for i in range(1000):
    if number%7==0 or number%9==0:
        print(str(i) + ": " + str(number))
        how_many+=1
        i+=1

    number+=1
            
    if how_many==25:
        print("lalalal")
        break