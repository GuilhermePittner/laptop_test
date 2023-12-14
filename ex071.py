amount = float(input('Digite o total de dinheiro: '))
restante = 1
notasCinquenta = notasVinte = notasDez = 0

while restante > 0:

    notasCinquenta = amount // 50
    restante = amount % 50

    if restante > 0:

        notasVinte = restante // 20
        restante = restante % 20

        if restante > 0:

            notasDez = restante // 10
            restante = restante % 10

            if restante > 0:
                
                print('Finalizando operação....')
                break

print(f'Você irá receber {notasCinquenta} notas de R$50, {notasVinte} notas de R$20, {notasDez} notas de R$10 e {restante} notas de R$1,')