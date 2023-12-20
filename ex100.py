import random


def somaPares(lista):
    soma = 0
    pares = ''

    for n in lista:
        if n%2 == 0:
            soma += n
            pares += f'{str(n)}, '

    print(f'Analisando a lista {lista} encontrei os seguintes valores pares: {pares}. E o valor obtido entre a soma deles foi de: {soma}')


def sorteia():
    lista = []

    for x in range(5):
        lista.append(random.randint(1, 100))

    somaPares(lista)


sorteia()
