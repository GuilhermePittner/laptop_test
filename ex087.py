
matriz = []
segunda_linha = []
pares = terceira_coluna = 0
 
for i in range (1,10):
    
    number = int(input(f'Diga o {i}° número: '))
    position = [number]

    if number%2 == 0:
        pares+=number

    if i in (3, 6, 9):
        terceira_coluna+=number

    if i in (4, 5, 6):
        segunda_linha.append(number)

    matriz.append(position)


text = ''
a = 0
for item in matriz:
    
    if a == 3:
        a = 0
        text += '\n'

    text += f'{item}'
    a+=1


print('\n')
print('voilá')
print(text)

print(f'A soma de todos os valores pares é: {pares}')
print(f'A soma de todos os valores da terceira coluna é: {terceira_coluna}')

segunda_linha.sort()
maior = segunda_linha[-1]
print(f'O maior valor da segunda linha é: {maior}')
