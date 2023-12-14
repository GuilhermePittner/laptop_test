import random

n1 = random.randint(0,1000)
n2 = random.randint(0,1000)
n3 = random.randint(0,1000)

if n1 > n2 and n2 > n3:
    print('n1 é maior que n2, que por sua vez é maior que n3')
elif n1 > n3 and n3 > n2:
    print('n1 é maior que n3, que por sua vez é maior que n2')
elif n2 > n1 and n1 > n3:
    print('n2 é maior que n1, que por sua vez é maior que n3')
elif n2 > n3 and n3 > n1:
    print('n2 é maior que n3, que por sua vez é maior que n1')
elif n3 > n1 and n1 > n2:
    print('n3 é maior que n1, que por sua vez é maior que n2')
elif n3 > n2 and n2 > n1:
    print('n3 é maior que n2, que por sua vez é maior que n1')

print(n1, n2, n3)

"""
n1, n2, n3



n1 > n2 > n3
n1 > n3 > n2

n2 > n1 > n3
n2 > n3 > n1

n3 > n1 > n2
n3 > n2 > n1
"""

