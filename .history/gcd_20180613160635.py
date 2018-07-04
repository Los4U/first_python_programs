print("The greatest common divisor")

fn = int(input("Input first number: "))
sn = int(input("Input second number: "))

def mygcd(a,b)
    while b!=0:
        if a > b:
            a = a - b
        else:
            b = b - a   
    return a

print("GDC for numbers:" , fn, " and ", sn, " = ", mygcd(fn, sn) )