while True:
    try:
        num1 = int(input("Enter a number (or a letter to exit) "))
        op = input("Enter an operation: +, -, *, / ")
        num2 = int(input("Enter another number: "))
        if op == "+":
            print("Result: " + str( num1 + num2) )
        elif op == "-":
            print("Result: " + str( num1 - num2) )
        elif op == "*":
            print("Result: " + str( num1 * num2) )
        elif op == "/":
            print("Result: " + str(num1 / num2) )#ZERO!!!!!!!!!!!!!!!!!
        else:
            print("Please define valid operation : +, -, *, /  ")
            continue        
    except ValueError:
        print("Koniec!")
        break
    except ZeroDivisionError:
        print("Pamiętaj cholero nie dziel przez Zero!")
        continue
