lista = []

while True:
    
    number = int(input('Digite um número: '))

    if number in lista:
        print('Opa! O número já existe na lista... Por favor, digite um valor diferente.')
        
        while number in lista:
            number = int(input('Digite outro número: '))

            if number in lista:
                print('Não insista. Eu disse para digitar um valor diferente.')
            else:
                lista.append(number)
                break

    else:
        lista.append(number)


    continuar = input('Deseja encerrar? Digite "S" caso queira interromper o programa.').upper()
    
    if continuar ==  'S':
        break

lista.sort()
print('Após uma sessão de digitação, sua lista ficou assim: ', lista)