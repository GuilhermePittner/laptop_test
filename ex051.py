print('=-'*12)
print('Termos de uma razão (Apenas os 10 primeiros)')
print('=-'*12)

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))


"""
ind = 0
for x in range(n1, 500000, n2):

    if ind == 10:
        break

    print(x)
    ind+=1
"""

ind=0
x = n1
while ind < 10:

    print(x)

    x += n2

    ind+=1

print('THE END!')
print('=-'*12)