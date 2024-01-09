l1 = float(input('Me diga o valor do primeiro segmento: '))
l2 = float(input('Me diga o valor do segundo segmento: '))
l3 = float(input('Me diga o valor do terceiro segmento: '))


if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    print('Oba! É possível montar um triângulo com as medidas citadas.')

    if l1 == l2 and l1 == l3:
        print('Aliás, este triângulo é equilátero.')

    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('Aliás, este triângulo é escaleno.')

    else:
        print('Aliás, este triângulo é isósceles.')

else:
    print('Com as medias inseridas, não é possível montar um triângulo.')


"""
Triângulo Isósceles:

Dois lados são iguais.
O terceiro lado é diferente.
"""