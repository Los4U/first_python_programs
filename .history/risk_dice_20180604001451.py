import random

def ron():
    return random.randrange(1,6)

print('Dice:')
#print('Attacker:'+ str(ron()) + "-")
#r = str(ron)
print('{0:<1} {1:>1} {2:>1}'.format(str(ron()),"-",str(ron())))