import random

names = []

names.append(input('Type one name... '))
names.append(input('Type another name... '))
names.append(input('And another... '))
names.append(input('Now the last one... '))

index = random.randint(0,3)
print(names[index])