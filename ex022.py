name = input('What is your full name? ')

print(name.upper())    # name in uppercase

print(name.lower())    # name in lowercase

print(len(name) - name.count(' '))    # name without blank spaces

splitted = (name.split())
print(len(splitted[0]))    # first name's len

