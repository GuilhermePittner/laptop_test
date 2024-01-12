msg = 'Sistema de ajuda do xuot1'

print('~' * (len(msg)+2))
print(msg)
print('~' * (len(msg)+2))


option = 'start'
while option != 'sair':
    
    option = str(input('Qual comando você deseja saber mais sobre? (Digite "sair" para encerrar.)').lower())
    print('\n')

    help(option)
    print('~' * 12)


msg = 'Obrigado por utilizar meu sistema de ajuda!'

print('~' * (len(msg)+2))
print(msg)
print('~' * (len(msg)+2))