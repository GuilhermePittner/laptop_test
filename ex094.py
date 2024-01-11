continuar = 'S'
contador = 0
pessoas = []

while continuar != 'N':
    contador+=1
    individuo = {}

    individuo['nome'] = str(input('Insira o nome da pessoa: '))
    sexo = str(input('Insira o sexo da pessoa [M/F]: ').upper())

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Por favor, responda com "M" ou "F". Insira o sexo da pessoa [M/F]: ').upper())
    
    individuo['sexo'] = sexo
    individuo['idade'] = int(input('Insira a idade da pessoa: '))

    continuar = str(input('Deseja continuar? [S/N]: ').upper())
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Por favor, responda com "S" ou "N". Deseja continuar? [S/N]: ').upper())
        break
    
    print('=-'*12)
    pessoas.append(individuo)


print('Contabilizando......')
print('=-'*12)

soma_idades = 0
nome_mulheres = ''

for person in pessoas:
    for chave, valor in person.items():
        
        # save the name to use on last IF
        if chave == 'nome':
            nome_atual = valor

        if chave == 'idade':
            soma_idades += valor

        if chave == 'sexo' and valor == 'F':
            nome_mulheres += f'{nome_atual}, '

media_idade = soma_idades/contador

print(f'Ao todo foram cadastradas {contador} pessoa(s).')
print(f'A média de idade foi: {media_idade:.2f} anos.')

if len(nome_mulheres) != 0:
    print(f'As mulheres cadastradas foi/foram: {nome_mulheres}')
else:
    print('Não foram cadastradas mulheres!')


lista_final = ''
for person in pessoas:
    for chave, valor in person.items():

        # save the name to use on last IF
        if chave == 'nome':
            nome_atual = valor

        if chave == 'sexo':
            sexo_atual = valor

        if chave == 'idade' and valor > media_idade:
            lista_final += f'nome = {nome_atual}; sexo = {sexo_atual}; idade = {valor}; \n'

if len(lista_final) != 0:
    print(f'Lista de pessoas que estão acima da média de idade. \n {lista_final}')
else:
    print('Nenhuma pessoa cadastrada estava acima da média de idade.')