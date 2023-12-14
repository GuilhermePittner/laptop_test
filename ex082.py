lista = []
listaOdd = []
listaEven = []

while True:
    
    number = int(input('Digite um número: '))
    lista.append(number)

    continuar = input('Deseja encerrar? Digite "S" caso queira interromper o programa.').upper()    
    if continuar ==  'S':
        break

for x in lista:
    if x % 2 == 0:
        listaEven.append(x)
    else:
        listaOdd.append(x)

print(f'Odd list: {listaOdd}')
print(f'Even list: {listaEven}')