"""
i did the exercise 51 using while, so here's the same code.
for now i'm going to do exercise 51 again, but now using a for loop.
"""


print('=-'*12)
print('Termos de uma razão (Apenas os 10 primeiros)')
print('=-'*12)

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))


ind=0
x = n1
while ind < 10:

    print(x)

    x += n2

    ind+=1

print('THE END!')
print('=-'*12)