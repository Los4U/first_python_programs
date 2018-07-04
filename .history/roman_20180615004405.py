'''
def arabic_to_roman(number):
    conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
            [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
            [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
            [   1, 'I']]
    result = ''
    for denom, roman_digit in conv:
        result += roman_digit*(number//denom)
        number %= denom
    return result

for i in 1,4,9,16,25,49,81,1963,2015:
    print(i, arabic_to_roman(i))
    '''
print("1000", 11//1000)
print("900", 11//900)
print("500", 11//500)
print("400", 11//400)
print("100", 11//100)
print("90", 11//90)
print("50", 11//50)
print("40", 11//40)
print("10", 11//10)
print("9", 11//9)
print("5", 11//5)
print("4", 11//4)
print("1", 11//1)