number  = 917
print("1000", number//1000)
print("900", number//900)
print("500", number//500)
print("400", number//400)
print("100", number//100)
print("90", number//90)
print("50", number//50)
print("40", number//40)
print("10", number//10)
print("9", number//9)
print("5", number//5)
print("4", number//4)
print("1", number//1)

change =    [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
            [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
            [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
            [   1, 'I']]
result = ''
for denom, roman_digit in change:

    result += roman_digit*(number//denom)
    number %= denom
    print(number , " - ", result)
