from datetime import datetime
current_year = datetime.now().year


def voto(year):
    age = (current_year - year)
    
    if age <= 17:
        status = 'proibido/negado.'

    elif age >= 70:
        status = 'opcional.'
        
    else:
        status = 'obrigatório.'

    return age, status


user_year = int(input('Qual ano você nasceu? '))

idade, situacao = voto(user_year)
print(f'Com {idade} anos, o voto é {situacao}')