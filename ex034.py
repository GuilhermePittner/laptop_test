salario = float(input('Diga-me seu salário: '))

if salario <= 1250:
    aumento = salario+(salario*0.15)
else:
    aumento = salario+(salario*0.10) 

print('Seu novo salário é: R${}'.format(aumento))