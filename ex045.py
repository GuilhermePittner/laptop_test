import random

moves = ['Rock', 'Paper', 'Scissors']
pc = moves[random.randint(0,2)]

player = int(input('Escolha uma jogada: \n 0 - Rock \n 1 - Paper \n 2 - Scissors '))
playerMove = moves[player]

too = False
if pc == playerMove:
    print('Its a draw!')
    too = True
elif playerMove == 'Rock' and pc == 'Paper':
    print('Computer wins!')
elif playerMove == 'Rock' and pc == 'Scissors':
    print('Player wins!')
elif playerMove == 'Paper' and pc == 'Rock':
    print('Player wins!')
elif playerMove == 'Paper' and pc == 'Scissors':
    print('Computer wins!')
elif playerMove == 'Scissors' and pc == 'Rock':
    print('Computer wins!')
elif playerMove == 'Scissors' and pc == 'Paper':
    print('Player wins!')

if too:
    print('Both player and computer choose {}.'.format(pc, playerMove))
else:
    print('Computer choose {} while player choose {}.'.format(pc, playerMove))