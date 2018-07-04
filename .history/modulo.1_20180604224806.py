number = 100
i = 1
how_many=0

rng = list(range(100,1000))
rng.reverse()


for i in rng:
    if number%7==0 or number%9==0:
        print(str(i) + ": " + str(number))
        how_many+=1
        i+=1

    number+=1
            
    if how_many==25:
        print("lalalal")
        break