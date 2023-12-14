import random

number = random.randint(0,10)
guess = 11
tries = 0

while guess != number:
    guess = int(input('Guess the number I am thinking! Give me one number: '))
    tries += 1
    if guess != number:
        print('Wrong! Cmon, try again.')

print('You guessed correctly! The number is {} and You tried {} times.'.format(number, tries))