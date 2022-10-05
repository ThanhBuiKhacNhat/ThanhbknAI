import random
def hi():
    if random.randint(0,1) == 0:
            return 'computer'
    else:
        return 'player'
print(hi())