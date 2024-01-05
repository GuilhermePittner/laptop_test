def resumo(value, increase, decrease):
    print('=-'*10)
    print('Resumo do valor...')
    print('=-'*10)
    print(f'Preço recebido: {value}')
    print(f'Dobro: {dobro(value, True)}')
    print(f'Metade: {metade(value, True)}')
    print(f'{increase}% de aumento: {aumentar(value, increase, True)}')
    print(f'{decrease}% de redução: {diminuir(value, decrease, True)}')
    print('=-'*10)


def aumentar(value, pctg, format=False):
    cifrao = "R$" if format else ""
    return f'{cifrao}{value + (value* (pctg/100) )}'


def diminuir(value, pctg, format=False):
    cifrao = "R$" if format else ""
    return f'{cifrao}{value - (value* (pctg/100) )}'
    
    
def dobro(value, format=False):
    cifrao = "R$" if format else ""
    return f'{cifrao}{value*2}'


def metade(value, format=False):
    cifrao = "R$" if format else ""
    return f'{cifrao}{value/2}'