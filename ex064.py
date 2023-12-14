flag = 0
soma = 0
numbers = 0

while flag != 999:
    flag = int(input('Give me one number: '))
    
    if flag != 999:
        soma += flag
        numbers += 1

print('You typed {} numbers and their sum is {}.'.format(numbers, soma))