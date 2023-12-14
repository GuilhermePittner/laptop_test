from datetime import date

today = date.today()
year = today.strftime("%Y")
year = int(year)

nascimento = int(input('Me diga em qual ano você nasceu... '))
idade = year-nascimento

if idade < 9:
    print('mirim')
elif idade >= 9 and idade < 14:
    print('infantil')
elif idade >= 14 and idade < 19:
    print('junior')
elif idade >= 19 and idade < 20:
    print('sênior')
else:
    print('veio assim e ainda quer nadar veinhokkkkkkk')