index = 1
genres = ['f','m']

while index != 0:
    gender = str(input('What is your gender? ')).lower()
    if gender not in genres:
        print('Gender not recognized... Please type again.')