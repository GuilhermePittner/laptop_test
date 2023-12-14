tupla = ('Corinthians', 'Cassio', 'Mundial', 'Poland')

for x in tupla:
    for y in x:
        if y.lower() == 'a' or y.lower() == 'e' or y.lower() == 'i' or y.lower() == 'o' or y.lower() == 'u':
            print(f'A letra {y} da palavra {x} é uma vogal.')
    print('+='*10)