print("The greatest common divisor")
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
while True:
    try:
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))
        print("The greatest common divisor of: " + str(a) + " i " + str(b) + " = " + str(gcd(a,b)) )
        break
    except ValueError: # przechwytuje wyjątek literę i kończy program.
        print("Please enter a number!")
        continue

