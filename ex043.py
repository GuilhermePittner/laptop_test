peso = float(input('Qual é o seu peso? (Em Kg): '))
altura = float(input('Qual é sua altura? (Ex: 1.78): '))


imc = peso / altura**2


print(f'Seu IMC: {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso.')

elif imc >= 18.5 and imc <= 25:
    print('Peso Ideal')

elif imc > 25 and imc <= 30:
    print('Sobrepeso')

elif imc > 30 and imc < 40:
    print('Obesidade')

else:
    print('Obesidade Mórbida')