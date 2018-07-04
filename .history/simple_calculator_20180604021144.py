#try:
num1 = input("Enter a number (or a letter to exit) ")

if num1.isdigit():
        op =   input("Enter an operation: ")
        num2 = int(input("Enter another number: "))
        if   op == "+":
            print( num1 + num2 )
        elif op == "-":
            print( num1 - num2 )
        elif op == "*":
            print( num1 * num2 )
        elif op == "/":
            print( num1 / num2 )
        else:
            print("cos")
else:
        print("koniec")

    #try:
    #    a = int(numstring)
    #    print("It's a number!")
    #except ValueError:
    #    print("It's not a number!")