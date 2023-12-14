import random

guess = int(input('Guess a number! '))
number = random.randint(0,5)

if guess == number:
    print('Congrats! You guessed the right number.')
else:
    print('I am sorry, you did not guess it right.')
    print('The choosen number was:', number)