"""
0,0 - 0,1 - 0,2
1,0 - 1,1 - 1,2
2,0 - 2,1 - 2,2
"""

matriz = []
for i in range (1,10):
    
    number = int(input(f'Diga o {i}° número: '))
    position = [number]

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