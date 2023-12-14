import random

n1 = random.randint(0,10)
n2 = random.randint(0,10)
n3 = random.randint(0,10)
n4 = random.randint(0,10)

tuplinha = (n1, n2, n3, n4)

print('Esta é a tupla:')
print(tuplinha)

print('Quantas vezes o número 9 apareceu: ')
print(tuplinha.count(9))

try:
    print('Primeira aparição do número 3.')
    print('Posição:', tuplinha.index(3))
except:
    print('O número 3 não existe nesta tupla.')

for x in tuplinha:
    if x % 2 == 0:
        print(x, 'faz parte da tupla e é par!.')    