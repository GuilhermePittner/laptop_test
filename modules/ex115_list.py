def consultarPessoas():
    with open('src/arquivo.txt', 'r') as f:
            linhas = f.readlines()
            for linha in linhas:
                nome, idade = linha.strip().split(',')
                print(f'{nome}, {idade} anos de idade.')


def cadastroPessoa():
    nome = str(input('Insira o nome da pessoa: '))
    idade = ''

    while not idade.isdigit():
        idade = input('Insira a idade da pessoa: ')

        if not idade.isdigit():
            print('O valor inserido não é um número... Por favor, tente novamente.')

    with open('src/arquivo.txt', 'a') as f:
        f.write(f'\n{nome},{idade}')