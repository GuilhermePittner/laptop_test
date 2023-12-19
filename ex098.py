def contador(start, end, step):

    # turns step 0 into 1
    if step == 0:
        print('Vou transformar esse passo 0 em 1, ok?')
        step = 1
    
    # check if step should decrease or increase
    if start > end:
        step = -1 * abs(step)

    # ???
    if start < end and step < 0:
        step = abs(step)

    print(f'Beleza, irei de {start} até {end} pulando de {abs(step)} em {abs(step)}')
    
    # end will be reached
    if step < 0:
        end -= 1
    else:
        end += 1


    for x in range(start, end, step):
        print(x, end=' ')
    print('END.')
    print('+='*15)


contador(0, 11, 1)
contador(10, -1, -2)


n1 = int(input('De qual número deseja começar? '))
n2 = int(input('Qual número deseja alcançar? '))
n3 = int(input('Quer "caminhar" de quanto em quanto? '))
print('+='*15)
contador(n1, n2, n3)
