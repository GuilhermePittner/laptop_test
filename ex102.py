def fatorial(num, show=False):
    res = 1
    math = ''

    for x in range(1, num+1, 1):
        res *= x
        math += f'{x} x '

    if show:
        return f'O fatorial de {num} detalhado é: {math[:-3]} = {res}'
    else:
        return f'O fatorial de {num} vale {res}'


print(fatorial(7, False))