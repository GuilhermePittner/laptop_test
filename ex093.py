sofascore = {}

sofascore['nome_jogador'] = str(input('Qual é o nome do monstro sagrado? '))
total_partidas = int(input('Quantas partidas essa lenda jogou? '))
lista_gols = []
total_gols = 0


for x in range(total_partidas):
    gols_jogo = int(input(f'Quantos gols o {sofascore["nome_jogador"]} fez no {x+1}° jogo? '))

    lista_gols.append(gols_jogo)
    total_gols += gols_jogo
print('=-'*12)

sofascore['jogador_lista_gols'] = lista_gols
sofascore['jogador_gols'] = total_gols

print(sofascore)
print('=-'*12)
      
print(f'O jogador se chama {sofascore["nome_jogador"]}')
print(f'O {sofascore["nome_jogador"]} anotou gols nessa sequência: {sofascore["jogador_lista_gols"]}')
print(f'Ao todo {sofascore["nome_jogador"]} anotou {total_gols} gols.')
print('=-'*12)


ind = 1
for y in sofascore["jogador_lista_gols"]:
    print(f'Na {ind}° partida {sofascore["nome_jogador"]} fez {y} gol(s)')
print(f'Resultando num total de {total_gols} gol(s).')