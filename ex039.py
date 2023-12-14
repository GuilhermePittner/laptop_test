from datetime import date

today = date.today()
year = today.strftime("%Y")
year = int(year)

nascimento = int(input('Me diga em qual ano você nasceu... '))

if (year - nascimento) < 18:
    print('Faltam',18-(year-nascimento),'ano(s) para você se alistar.')
elif (year - nascimento) == 18:
    print('Está na idade de se alistar!')
else:
    print('Você já se alistou? Não? Então está atrasado em',(year-nascimento)-18,'anos.')