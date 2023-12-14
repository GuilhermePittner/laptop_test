numbersList = [[], []]


for i in range(1,8):
    value = int(input(f'Insira o {i}° valor: '))
    
    if value % 2 == 0:
        numbersList[0].append(value)
    else:
        numbersList[1].append(value)


#sorted_numbers = sorted(numbers, reverse=True)

print(f'Lista com os pares: {sorted(numbersList[0])}')
print(f'Lista com os ímpares: {sorted(numbersList[1])}')

"""
for number in numbersList:
    
    if int(number) % 2 == 0:
        print(f'{number} é par')
    else:
        print(f'{number} é ímpar')
"""