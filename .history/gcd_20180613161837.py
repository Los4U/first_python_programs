print("The greatest common divisor")

def mygcd(a,b):
    while b!=0:
        if a > b:
            a = a - b
        else:
            b = b - a   
    return a
test = True
while True:
    try:
        fn = int(input("Input first number: "))
        if str(fn) == "q":
            break
        else:
            sn = int(input("Input second number: "))
            print("GCD for numbers:" , fn, ",", sn, " = ", mygcd(fn, sn), "\n" )
    except ValueError: 
        print("Please enter a number!")
        continue


