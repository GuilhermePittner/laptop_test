flag = 'T'
soma = numbers = highest = lowest = 0
first = True

while flag != 'F':
    
    if flag == 'T':
        number = int(input('Insert value: '))
        soma += number
        numbers += 1

        if first:
            first = False
            highest = lowest = number

            number = int(input('Insert another value: '))
            soma += number
            numbers += 1

        if number > highest:
            highest = number

        if number < lowest:
            lowest = number

        flag = str(input('Do you wanna insert another value? [T/F]')).upper()
    else:
        flag = str(input('You need to type T to continue or F to stop! Please, try again. [T/F]')).upper()

print('Average: {}, Highest: {}, Lowest: {}'.format(soma/numbers, highest, lowest))
