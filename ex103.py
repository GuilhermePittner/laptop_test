def ficha(name=False, points=False):
    
    if not name and not points:
        print(f'O jogador <desconhecido> não marcou um gol sequer.')

    elif not name:
        print(f'O jogador <desconhecido> marcou {points} gol(s).')

    elif not points:
        print(f'O jogador {name} não marcou um gol sequer.')

    else:
        print(f'O jogador {name} marcou {points} gol(s).')


ficha('Roger Guedes', 271)
ficha('', '')
ficha('Yuri Alberto')
ficha('', 22)


player = str(input('Insira um jogador: '))
goals = int(input('Quantos gols ele fez? '))
ficha(player, goals)