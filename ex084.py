turma = list()
pessoa = list()

maiores = menores = ''

cont = 0

while True:
    pessoa.append(str(input('Digite um nome: ')))
    pessoa.append(int(input('Digite o peso: ')))

    turma.append(pessoa[:])
    cont+=1
    pessoa.clear()

    choice = str(input('Deseja interromper? Digite "S"')).upper()
    if choice == 'S':
        break

maiorPeso = list()
menorPeso = list()
for x in turma:
   
    if len(menorPeso) == 0 or x[1] < menorPeso[0]:
        menorPeso.clear()
        menorPeso.append(x[1])

        menores = ''
        menores += x[0] + ', '
    elif x[1] == menorPeso[0]:
        menores += x[0] + ', '

    if len(maiorPeso) == 0 or x[1] > maiorPeso[0]:
        maiorPeso.clear()
        maiorPeso.append(x[1])

        maiores = ''
        maiores += x[0] + ', '
    elif x[1] == maiorPeso[0]:
        maiores += x[0] + ', '

print(f'O maior peso registrado foi de {maiorPeso[0]}kg pela(s) pessoa(s) {maiores}')
print(f'O menor peso registrado foi de {menorPeso[0]}kg pela(s) pessoa(s) {menores}')
print(f'Foram cadastrados(as) {cont} pessoas.')


