import random
def ron():
    return random.randrange(1,6)
print('Dice:')

print('{0} {1} {2} {3} {4} {5}'.format("Attacker: ", str(ron()),"-",str(ron()),"-",str(ron()) ))