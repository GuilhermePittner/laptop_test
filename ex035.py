# triangles

l1 = float(input('Me diga o valor do primeiro segmento: '))
l2 = float(input('Me diga o valor do segundo segmento: '))
l3 = float(input('Me diga o valor do terceiro segmento: '))


if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('Oba! É possível montar um triângulo com as medidas citadas.')
else:
    print('Com as medias inseridas, não é possível montar um triângulo.')


"""
easier solution
if l1 < l2+l3 and l2 < l1+l3 and l3 < l2+l1:
    print('Oba! É possível montar um triângulo com as medidas citadas.')
"""


"""
- my solution (not working)


if (l1+l2) < l3 or (l1+l3) < l2 or (l2+l3) < l1:
    print('Com as medias inseridas, não é possível montar um triângulo.')
elif abs(l1-l2) > l3 or abs(l1-l3) > l2 or abs(l3-l2) > l1:
    print('Com as medias inseridas, não é possível montar um triângulo.')
else:
    print('Oba! É possível montar um triângulo com as medidas citadas.')

2
4
6

2+4 < 6
2+6 < 4
4+6 < 2


- my solution (fixed)

if (l1+l2) <= l3 or (l1+l3) <= l2 or (l2+l3) <= l1:
    print('Com as medias inseridas, não é possível montar um triângulo.')
else:
    print('Oba! É possível montar um triângulo com as medidas citadas.')
"""