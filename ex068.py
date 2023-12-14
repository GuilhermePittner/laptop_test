import random

wins = 0
game = True

while game:

    print('+='*10)
    player_number = int(input('Digite um número. '))
    player_choice = input('Par ou ímpar? [P/I]').upper()
    ndFlag = False

    while ndFlag == False:

        if player_choice == 'I':
            computer_choice = 'P'
            ndFlag = True
            break

        elif player_choice == 'P':
            computer_choice = 'I' 
            ndFlag = True
            break

        else:
            player_choice = input('Você precisa escolher entre P ou I !').upper()
    
    computer_number = random.randint(0,1000)
    if (computer_number+player_number) % 2 == 0:
        print(f'O computador escolheu o número {computer_number}! E a soma entre {computer_number} e {player_number} é {player_number+computer_number}. Portanto, o resultado é par!')
        result = 'P'
        print('+='*10)
    else:
        print(f'O computador escolheu o número {computer_number}! E a soma entre {computer_number} e {player_number} é {player_number+computer_number}. Portanto, o resultado é ímpar!')
        result = 'I'
        print('+='*10)
    
    if result == player_choice:
        print(f'Parabéns! Você venceu após escolher {result}!')
        wins += 1
    else:
        print(f'Xiii! Você foi derrotado após escolher {result}!')
        
        if wins == 0:
            print(f'Fim de jogo! Você foi derrotado logo de cara... Que azar.')
        elif wins == 1:
            print(f'Fim de jogo! Você venceu apenas uma vez.')
        else:
            print(f'Fim de jogo! Você venceu {wins} vezes.')  

        print('Obrigado por jogar!')
        game = False