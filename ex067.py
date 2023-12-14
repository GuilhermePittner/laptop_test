while True:
    print('+='*10)
    n = int(input('Escolha um número para ver sua tabuada! '))

    if n < 0:
        break

    print('+='*10)
    for i in range(0, 11):
        print(f'{n}*{i}={n*i}')