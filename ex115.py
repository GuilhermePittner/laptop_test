from modules.ex115_list import *

def sistemaDeCadastro():
    
    option = 1

    print('=-'*12)
    print('Bem vindo ao sistema. O que deseja fazer?')
    print('1 - Consultar usuários.')
    print('2 - Novo cadastro.')
    print('3 - Sair.')

    while option != 3:
        
        try:
            print('=-'*12)
            option = int(input('Selecione uma opção: '))

            if option == 1:
                print('Consultando base de dados......')
                print('=-'*12)

                consultarPessoas()

            elif option == 2:
                print('Seguindo para o cadastro.......')
                print('=-'*12)

                cadastroPessoa()

            elif option == 3:
                break

            else:
                print('O valor inserido não corresponde a uma opção... Por favor, tente novamente.')

        except:
            print('O valor inserido não corresponde a uma opção... Por favor, tente novamente.')

    print('=-'*12)
    print('Obrigado por usar nosso sistema!')


sistemaDeCadastro()