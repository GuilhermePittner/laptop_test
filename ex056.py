avg = 0
femaleCount = 0
manAge = 0
manName = ''

for i in range(0,4):
    name = str(input('What is your name? '))
    age = int(input('How old are you? '))
    gender = str(input('What is your gender? (M/F) '))

    avg += age
    if gender.lower() == 'f' and age < 20:
        femaleCount += 1

    if gender.lower() == 'm' and age > manAge:
        manName = name

print('Average: {}'.format(avg/4))
print('This group has {} woman/women 19 years old or lower.'.format(femaleCount))

if manName != '':
    print('The oldest man is named {}.'.format(manName))
else:
    print('There is no guys in your click.')