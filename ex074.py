import random

n1 = random.randint(0,1000)
n2 = random.randint(0,1000)
n3 = random.randint(0,1000)
n4 = random.randint(0,1000)
n5 = random.randint(0,1000)

tuplinha = (n1, n2, n3, n4 ,n5)

print('Esta é a tupla:')
print(tuplinha)

print('Este é o menor número da tupla')
print(sorted(tuplinha)[0])

print('Este é o maior número da tupla')
print(sorted(tuplinha)[len(tuplinha)-1])