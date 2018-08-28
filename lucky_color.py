import random

colors = ['red', 'blue', 'green', 'purple', 'yellow']
luckyColor = random.choice(colors)
for i in range(3):
    print('There are {} colors.'.format(colors))
    guess = input('What is your lucky color? ')
    if guess != luckyColor:
        print('Oh no! {} is not your lucky color!'.format(guess))
        colors.remove(guess)
    else:
        break

if guess == luckyColor:
    print('Great! {} is your lucky color.'.format(guess))
else:
    print('Actually {} is your lucky color.'.format(luckyColor))
