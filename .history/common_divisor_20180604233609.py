print("The greatest common divisor")
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("Please enter the first number: "))
a = int(input("Please enter the second number: "))
print("The greatest common divisor of: " + str(a) + " i " + str(b) + " = " + gcd(a,b) )

