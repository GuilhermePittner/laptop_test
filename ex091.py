import random

my_dict = {}


for x in range(1, 5):
    random_integer = random.randint(1, 6)
    my_dict[f'jogador_{x}'] = random_integer


list_names = []
list_values = []

sorted_dict_by_values = dict(sorted(my_dict.items(), reverse=True, key=lambda item: item[1]))
r = 1
for k, v in sorted_dict_by_values.items():
    print(f'{k} ficou em {r}° pois tirou o número {v}')
    r+=1