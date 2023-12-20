def maior(*numbers):

    if len(numbers) == 0:
        print('Nenhum valor foi passado!')
        return
        
    if len(numbers) == 1:
        print(f'Apenas um valor foi passado, aqui está o (lógicamente) maior: {numbers[0]}')

    else:
        print(f'Opa, recebi tudo isso: {numbers} e vou descobrir qual é o maior.')
        maior = -999999999999999

        for n in numbers:

            if n > maior:
                maior = n
                print(f'Novo maior: {maior}')

        print(f'Finalizei minha checagem! O maior número entre {numbers} é o {maior}')
    print('=-'*15)


maior(5, 8, 2, 8, 0, 1, 12, 78, 2, 9, 32, 12)
maior(1, 8, 3, 7)
maior(90, 89)
maior(0)
maior(9, 0)
maior()
maior(-5, -9)