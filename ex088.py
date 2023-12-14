import random, time

megasena = list()
jogo = list()

qtdJogos = int(input('Quantos jogos deseja gerar? '))
for y in range(1, qtdJogos+1):
    for i in range(0,6):

        gerado = random.randint(0,60)
        if gerado not in jogo:
            jogo.append(gerado)
        else:
            while gerado in jogo:
                gerado = random.randint(0,60)

                if gerado not in jogo:
                    jogo.append(gerado)
                    break

    jogo.sort()
    print(f'{y}o jogo: {jogo}')
    time.sleep(1)
    jogo.clear()

