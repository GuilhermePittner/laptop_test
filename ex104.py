"""
first attempt
"""

def leiaInt(text):
    value = input(text)
    
    if value.isdigit():
        value = f'O número digitado foi: {int(value)}'
    
    else:
        value = 'O valor inserido não é um número.'

    return value


n = leiaInt('Digite um valor: ')
print(n)

"""
then i saw the video...

def leiaInt(text):
    value = input(text)
    check = False

    while check == False:
    
        if value.isdigit():
            value = f'O número digitado foi: {int(value)}'
            check = True

        else:
            print('\033[0;31mO valor inserido não é um número.\033[m')
            # hmm colors :)
            
            text = 'Digite outro valor: '
            value = input(text)

    return value


n = leiaInt('Digite um valor: ')
print(n)
"""