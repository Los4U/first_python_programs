print("top 25 three-digit natural numbers divisible by 7 or by 9")
ra = list(range(100,1000))
ra.reverse()

count = 1
for i in ra:
    if i%7==0 or i%9==0:
        print(str(count) + ": " + str(i))
        count+=1
    if count==26:
        print("End")
        break