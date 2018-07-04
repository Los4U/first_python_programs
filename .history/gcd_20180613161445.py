print("The greatest common divisor")

def mygcd(a,b):
    while b!=0:
        if a > b:
            a = a - b
        else:
            b = b - a   
    return a

while True:
    try:
        fn = int(input("Input first number: "))
        sn = int(input("Input second number: "))
        print("GDC for numbers:" , fn, " and ", sn, " = ", mygcd(fn, sn), "\n" )
    except ValueError: 
        print("Please enter a number!")
        continue


