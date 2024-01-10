print('=-'*12)
print('Termos de uma razão v.3.0')
print('=-'*12)


n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))


total = 0
again = 10
while again != 0:

    ind = 0
    for x in range(n1, n2*10000, n2):

        if ind == again:
            break

        print(x, end=' --> ')
        ind+=1

    again = int(input('\n Quantos termos você deseja ver a mais? Digite 0 caso queira encerrar: '))
    n1 = x
    total += ind


print('=-'*12)
print(f'Ok, foram mostrados {total} termos. Até mais.')