lista = []
cont = 0

while True:
    
    number = int(input('Digite um número: '))
    lista.append(number)
    cont+=1

    continuar = input('Deseja encerrar? Digite "S" caso queira interromper o programa.').upper()    
    if continuar ==  'S':
        break

lista.sort(reverse=True)

print('=+'*20)

print('Após uma sessão de digitação, sua lista ficou assim: ', lista)
print(f'Você digitou {len(lista)} números.')


if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não existe nessa lista.')