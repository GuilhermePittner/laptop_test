from modules import ex108_coin

pounds = float(input('Me diga um valor... (Ex: 100): '))

print(f'A metade de R${pounds} é R${ex108_coin.metade(pounds)}')
print(f'O dobro de R${pounds} é R${ex108_coin.dobro(pounds)}')
print(f'Aumentando R${pounds} em 10% temos R${ex108_coin.aumentar(pounds, 10)}')
print(f'Diminuindo R${pounds} em 13% temos R${ex108_coin.diminuir(pounds, 13)}')