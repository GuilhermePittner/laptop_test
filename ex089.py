alunos = list()
boletim = list()
codigo=-1

while True:
    nome = (str(input('Insira um nome: ')))
    n1 = (float(input('Insira a primeira nota: ')))
    n2 = (float(input('Insira a segunda nota: ')))
    media = (n1+n2)/2
    codigo+=1

    individual = [codigo, nome, [n1,n2]]
    alunos.append(individual[:])

    notas = [codigo, nome, media]
    boletim.append(notas[:])
    
    individual.clear()
    notas.clear()
    
    choice = str(input('Deseja interromper? "S" para parar.')).upper()
    if choice == 'S':
        break

print('+=+=+ Boletim +=+=+')

for x in boletim:
    print(f'Aluno {x[1]} de código {x[0]} obteve a média {x[2]}')

menu = 0
while menu != 999:
    menu = int(input('Deseja ver o boletim detalhado de qual aluno? (Digite 999 para sair)'))

    if menu > len(alunos)-1:
        print('Opa! Você digitou um número de aluno inexistente... Tente novamente.')
    else:
        print(alunos[menu])

print('+=+=+ Encerrando boletim +=+=+')