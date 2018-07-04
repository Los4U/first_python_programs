import random
def ron():
    return random.randrange(1,6)
print('Dice:')
#print('Attacker:'+ str(ron()) + "-")
print('{0:<4} {1:>3}'.format("Attacker:",ron))
#print('Defender:' )


#print('{0:<4} {1:>30}'.format(str(fn) + ":", fib))