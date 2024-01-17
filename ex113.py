def leiaInteiro(text):

    value = input(text)
    check = False

    while check == False:
    
        if value.isdigit():
            value = f'O número inteiro digitado foi: {int(value)}'
            check = True

            print('~'*12)

        else:
            print('\033[0;31mO valor inserido não é um número inteiro.\033[m')
            # hmm colors :)
            
            text = 'Digite outro valor: '
            value = input(text)

    return value


n = leiaInteiro('Digite um número inteiro: ')
print(n)


def leiaReal(text):

    value = input(text)
    check = False

    while check == False:

        try:
            value = float(value)
            value = f'O número real digitado foi: {int(value)}'
            check = True

            print('~'*12)

        except ValueError:
            print('\033[0;31mO valor inserido não é um número real.\033[m')

            text = 'Digite outro valor: '
            value = input(text)
    
    return value

#n = leiaReal('Digite um número real: ')
#print(n)