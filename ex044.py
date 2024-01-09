valor = float(input('Qual é o valor total da compra? R$'))
print('=-'*12)
print('Como deseja efetuar o pagamento?')
print('=-'*12)


choice = int(input(('Tecle (1) para pagamento à vista dinheiro/pix. (10% de desconto) \n'
    'Tecle (2) para pagamento à vista no cartão. (5% de desconto) \n'
    'Tecle (3) para pagamento em até 2x no cartão. (Preço normal) \n'
    'Tecle (4) para pagamento em 3x ou mais no cartão. (20% de juros) \n'
    'Opção desejada: '
    )))
print('=-'*12)


match choice:
    case 1:
        price = valor - valor*0.1
        print(f'Você selecionou pagamento à vista/pix. Neste caso terá 10% de desconto. Assim, o valor final será de: R${price}')

    case 2:
        price = valor - valor*0.05
        print(f'Você selecionou pagamento à vista no cartão. Neste caso terá 5% de desconto. Assim, o valor final será de: R${price}')

    case 3:
        price = valor / 2
        print(f'Você selecionou parcelar em duas vezes no cartão. Neste caso pagará o valor cheio em duas parcelas de R${price}. Assim, o valor final continuará R${valor}')

    case 4:
        parcelas = int(input('Você selecionou para parcelar em 3 ou mais vezes. Quantas parcelas deseja fazer? '))

        while parcelas <= 2:
            parcelas = int(input('O número mínimo de parcelas é 3. Por favor, insira quantas parcelas deseja fazer: '))

        price = valor + (valor * 0.2)
        valor_parcela = price / parcelas
        print(f'Você dividiu o valor de R${valor} em {parcelas} parcelas. Aplicando o juros de 20%, o valor final ficará R${price}, com cada parcela valendo R${valor_parcela}') 
        

    case _:
        print('Não aceitamos calote!! Saia daqui imediatamente.')