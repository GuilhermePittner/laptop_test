n1 = int(input('n1 '))
n2 = int(input('n2 '))

if n1 > n2:
    print('{} é maior que {}'.format(n1,n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2,n1))
else:
    print('Os números são iguais!')