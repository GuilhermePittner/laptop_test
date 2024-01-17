from pacote_gui import moeda

pounds = float(input('Me diga um valor... (Ex: 100): '))

print(f'Half: {moeda.metade(pounds)}')
print(f'Double: {moeda.dobro(pounds)}')
print(f'Increasing 10%: {moeda.aumentar(pounds, 10)}')
print(f'Reducing 13%: {moeda.diminuir(pounds, 13)}')