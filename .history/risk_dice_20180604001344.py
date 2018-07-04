import random

def ron():
    return random.randrange(1,6)

print('Dice:')
#print('Attacker:'+ str(ron()) + "-")
#r = str(ron)
print('{0:<4} {1:>3}'.format(str(ron()),str(ron())))