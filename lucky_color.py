import random

colors = ['red', 'blue', 'green', 'purple', 'yellow']
luckyColor = random.choice(colors)

for i in range(3):
    print('There are {} colors'.format(colors))
    guess = input('Guess your luck color: ')
    if guess != luckyColor:
        print('Seems like {} is not your luck color:('.format(guess))
        colors.remove(guess)
    else:
        break
