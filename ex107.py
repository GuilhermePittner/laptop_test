from modules import ex107_coin

pounds = float(input('Me diga um valor... (Ex: 100): '))

print(f'Half: {ex107_coin.metade(pounds)}')
print(f'Double: {ex107_coin.dobro(pounds)}')
print(f'Increasing 10%: {ex107_coin.aumentar(pounds, 10)}')
print(f'Reducing 13%: {ex107_coin.diminuir(pounds, 13)}')