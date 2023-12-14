total = caros = 0
cheapest = ''

while True:
    print('=+'*10)

    name = input('Nome do produto. ')
    price = float(input('Preço do produto. '))

    total += price

    if price > 1000:
        caros += 1

    if cheapest == '':
        cheapest = name
        cheapestValue = price
    
    else:
        if price < cheapestValue:
            cheapest = name
            cheapestValue = price

    choice = input('Deseja parar? Digite [S]').upper()
    if choice == 'S':
        break

print(f'O total da compra foi de {total} e o produto mais barato foi {cheapest}. Além disso, {caros} produtos custaram mais de R$1000.00')