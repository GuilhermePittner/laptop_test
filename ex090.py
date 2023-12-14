my_dict = {}

student_name = str(input('Qual é o nome do aluno? '))
student_average = int(input('Qual foi a média do aluno? '))

my_dict['nome'] = student_name
if student_average >= 7:
    my_dict['situação'] = 'aprovado'
else:
    my_dict['situação'] = 'reprovado'


for key, value in my_dict.items():
    print(f'Na posição {key} temos o valor {value}')