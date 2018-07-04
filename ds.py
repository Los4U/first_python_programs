import sys
inp = input("Input a number(arabic one) between 1 and  4000 that you want to be transfered to roman form.")
try:
   val = int(inp)
except ValueError:
   sys.exit(print("That's not a number!"))

num = int(inp)
print(num)
if num < 4001:
    rom = 'I' * num
    print(rom)
    rom = rom.replace('I'*5, 'V')
    print(rom)
    rom = rom.replace('V'*2, 'X')
    print(rom)
    rom = rom.replace('X'*5, 'L')
    print(rom)
    rom = rom.replace('L'*2, 'C')
    print(rom)
    rom = rom.replace('C'*5, 'D')
    print(rom)
    rom = rom.replace('D'*2, 'M')
    print(rom)

    rom = rom.replace("DCCCC", "CM")
    print(rom)
    rom = rom.replace("CCCC", "CD")
    print(rom)
    rom = rom.replace("LXXXX", "XC")
    print(rom)
    rom = rom.replace("XXXX", "XL")
    print(rom)
    rom = rom.replace("VIIII", "IX")
    print(rom)
    rom = rom.replace("IIII", "IV")
    print(rom)
else:
    print("Input a number between 1 and 4000!")