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