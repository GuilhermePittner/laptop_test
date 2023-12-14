number = int(input('Qual número deseja converter? '))
option = int(input('Para qual base deseja converter? (Escolha entre 1, 2 e 3.) '))

if option == 1:
    result = bin(number)
    base = 'binário'

elif option == 2:
    result = oct(number)
    base = 'octal'

elif option == 3:
    result = hex(number)
    base = 'hexadecimal'

else:
    print('Ops... Você deve escolher uma opção entre 1, 2 e 3.')
    base = False

if base:
    print('O número {} na base {} é: {}'.format(number, base, result))