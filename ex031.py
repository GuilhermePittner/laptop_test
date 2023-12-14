distance = float(input('Qual foi a distancia percorrida? (Em Km) '))

if distance <= 200:
    print('O custo da viagem foi de:',(distance*0.50))
else:
    print('O custo da viagem foi de:',(distance*0.45))