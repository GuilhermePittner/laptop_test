def getAmount(text="Insira o valor em R$"):

    value = input(text)
    check = False

    while check == False:
    
        if value.isdigit():
            #print(f'inteiro - R${value}')
            check = True

            print('~'*12)
            return value

        else:

            try:
                value = float(value)
                #print(f'real - R${value}')
                check = True

                print('~'*12)
                return value

            except ValueError:

                if ',' in value:
                    value = value.replace(',', '.')
                    #print(f'real - R${value}')
                    check = True

                    print('~'*12)
                    return value

                else:
                    print('\033[0;31mO valor inserido não é um número.\033[m')

                    text = 'Insira o valor em R$'
                    value = input(text)

def dinheiroGeral(value):
    print('=-'*12)
    aumentar(value)
    diminuir(value)
    metade(value)
    dobro(value)
    print('=-'*12)

def aumentar(value, pctg=10):
    print(f'Aumentando R$ {value} em {pctg}% teremos: R$ {value + (value* (pctg/100) )}')

def diminuir(value, pctg=13):
    print(f'Diminuindo R$ {value} em {pctg}% teremos: R$ {value - (value* (pctg/100) )}')

def dobro(value):
    print(f'O dobro de R$ {value} é R${value*2}')

def metade(value):
    print(f'A metade de R$ {value} é R${value/2}')