lista = []
sortedLista = []

for i in range(0,5):
    lista.append(int(input('Digite um número: ')))

sortedLista = lista[:]
sortedLista.sort()

print(lista)
print(f'O menor número digitado foi {sortedLista[0]} na posição {lista.index(sortedLista[0])}.')
print(f'O maior número digitado foi {sortedLista[4]} na posição {lista.index(sortedLista[4])}.')

