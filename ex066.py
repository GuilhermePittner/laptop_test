soma = cont = 0
while True:
    n = int(input('Give me a number! (Type 999 to exit.) '))
    
    if n == 999:
        break
    else:
        soma += n
        cont += 1

if cont == 0:
    print('You did type any number! Try again, but this time give me some numbers.')
else:
    print(f'You entered {cont} numbers and their sum is {soma}.')