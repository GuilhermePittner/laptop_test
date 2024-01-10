n = int(input('Quantos números da sequência você deseja ver? '))


if n == 1:
    print('0', end=' --> ')

elif n < 1:
    print('Por favor, na próxima escolha um número natural (exceto 0).')

else:
    print('0 --> 1', end=' --> ')
    for x in range(n-2):

        if x == 0:

            a = 0
            b = 1

            d = b
            b = c = a+b
            a = d

            #print(f'c é {c} \n a é {a} \n b é {b}')
            print(c, end=' --> ')

        else:
            d = b
            b = c = a+b
            a = d

            #print(f'c é {c} \n a é {a} \n b é {b}')
            print(c, end=' --> ')

print('fim.')
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987


#1 + 0 = 1
#x+y=z
#
#1+1=2
#z+x=w
#
#2+1=3
#
#3+2=5
