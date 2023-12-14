price = int(input('Valor da casa '))
salary = int(input('Salário '))
years = int(input('How many years will it take? '))

prestacoes = years * 12
valor = price/prestacoes

print('O valor de cada prestação será de R${}.'.format(round(valor,2)))
if valor > (salary+salary*0.3):
    print('Lamento mas o valor das prestações ficaram muito altos em comparação com seu salário.')
else:
    print('Oba! Iremos aprovar seu empréstimo.')
