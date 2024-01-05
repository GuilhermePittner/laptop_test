from modules import ex109_coin

pounds = float(input('Me diga um valor... (Ex: 100): '))

print(f'A metade de R${pounds} é {ex109_coin.metade(pounds, True)}')
print(f'O dobro de R${pounds} é {ex109_coin.dobro(pounds, True)}')
print(f'Aumentando R${pounds} em 10% temos {ex109_coin.aumentar(pounds, 10, True)}')
print(f'Diminuindo R${pounds} em 13% temos {ex109_coin.diminuir(pounds, 13, True)}')