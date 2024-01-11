sofascore = {}
#sofascore = {'atleta_0': [0, 'romero', [1, 2, 3], 6], 'atleta_1': [1, 'roger guedes', [5, 5, 5, 5, 5], 25]}
continuar = 'S'
contador = 0

while continuar != 'N':
    
    total_gols = 0

    jogador_informacoes = []
    jogador_gols = []

    jogador_informacoes.append(contador)

    jogador_informacoes.append(str(input('Qual é o nome do monstro sagrado? ')))

    total_partidas = int(input(f'Quantas partidas o {jogador_informacoes[1]} jogou? '))

    for x in range(total_partidas):
        gols_jogo = int(input(f'Quantos gols o {jogador_informacoes[1]} fez no {x+1}° jogo? '))
        total_gols += gols_jogo
        jogador_gols.append(gols_jogo)

    continuar = str(input('Deseja continuar? [S/N]: ').upper())

    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Por favor, responda com "S" ou "N". Deseja continuar? [S/N]: ').upper())

    jogador_informacoes.append(jogador_gols)
    jogador_informacoes.append(total_gols)

    sofascore[f'atleta_{contador}'] = jogador_informacoes
    contador+=1

    print('=-'*12)


print('Calculando...')

print('=-'*12)
print('id    nome     gols      total')
print('-----------------------------')
for chave in sofascore.values():

    for values in chave:
        print(values, end=' ')
        
    print('\n')


levantamento = 1
while levantamento != 999:

    levantamento = int(input('Quer ver o levantamento de qual jogador? (999 encerra o programa): '))
    
    try:
        info_levantamento = sofascore[f'atleta_{levantamento}']
        print('=-'*12)

        print(f'Mega levantamento do jogador {info_levantamento[1]}:')
        for indice, gols in enumerate(info_levantamento[2]):
            print(f'Na {indice+1}° partida,  {info_levantamento[1]} fez {gols} gol(s).')
        print('=-'*12)

    except:
        print('Não há um jogador com este ID... Por favor, tente novamente.')


print('=-'*12)
print('Finalizando Execução.')