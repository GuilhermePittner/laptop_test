from datetime import datetime
current_year = datetime.now().year


my_dict = {}


my_dict['user_name'] = str(input('Qual é o seu nome? '))

user_year = int(input('Em qual ano você nasceu? '))
my_dict['user_age'] = current_year-user_year

user_ctps = int(input('Me passa sua CTPS rapidão pra eu ver um negócio. (Digite 0 caso não possua) '))

if user_ctps != 0:
    my_dict['user_ctps'] = user_ctps

    my_dict['user_employed'] = int(input('Em qual ano você foi contratado?'))
    tempo_contribuido = current_year - my_dict['user_employed']

    my_dict['user_retired'] = current_year-user_year + 35 - (tempo_contribuido)
    
    my_dict['user_salary'] = int(input('Fala seu salário aí para eu fazer uma simulação de financiamento: '))

my_dict['user_ctps'] = user_ctps
print("+=+="*15)
for k,v in my_dict.items():
    print(f'Casa {k} valor {v}')
print("+=+="*15)



# Qual é o seu nome? creuza
# Em qual ano você nasceu? 1999
# Me passa sua CTPS rapidão pra eu ver um negócio. (Digite 0 caso não possua) 43
# Fala seu salário aí para eu fazer uma simulação de financiamento: 3000
# Em qual ano você foi contratado?2015
