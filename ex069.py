gender = ''
choice = 'Y'
maiores = homens = mulheres = 0

while True:

    age = int(input('Insira sua idade. '))
    if age > 18:
        maiores += 1

    gender = input('Qual é seu gênero? Escolha entre M ou F [M/F] ').upper()
    ndFlag = False

    while ndFlag == False:

        if gender == 'M':
            homens += 1
            ndFlag = True
            break

        elif gender == 'F':
            ndFlag = True

            if age < 20:
                mulheres += 1

            break

        else:
            gender = input('Errado... Escolha entre M ou F [M/F] ').upper()


    choice = input('Deseja encerrar o programa? Digite N para encerrar. (Qualquer outra tecla continuará a execução.)').upper()

    if choice == 'N':
        break

    print('+='*10)

print('+='*10)
print(f'Temos {maiores} maiores de idade, {homens} homens cadastrados e {mulheres} mulheres menores de 20 anos.')