import math
while True:
    try:
        num1 = int(input("Enter a number (or a letter to exit) "))
        op = input("Enter an operation: +, -, *, / , pow")
        num2 = int(input("Enter another number: "))
        if op == "+":
            print("Result: " + str(num1 + num2))  # dodawanie
        elif op == "-":
            print("Result: " + str(num1 - num2))
        elif op == "*":
            print("Result: " + str(num1 * num2))
        elif op == "/":
            print("Result: " + str(num1 / num2))  # ZERO!!!!!
        elif op == "pow":
            print("Result: " + str(math.pow(num1, num2)))  # potęga x do y
        else:
            print("Please define valid operation : +, -, *, /  ")
            continue
    except ValueError:  # przechwytuje wyjątek literę i kończy program.
        print("Exit!")
        break
    # przechwytuje wyjątek dzielenie przez zero i wznawia program.
    except ZeroDivisionError:
        print("Pamiętaj cholero nie dziel przez Zero!")
        continue
