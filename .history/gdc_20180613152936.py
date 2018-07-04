
fn = int(input("Input first number: "))
sn = int(input("Input second number: "))

a = fn
b = sn

while b!=0:
    if a > b:
        a = a - b
    else:
        b = b - a    

print("GDC for numbers:" , fn, " and ", sn, " = ", a )