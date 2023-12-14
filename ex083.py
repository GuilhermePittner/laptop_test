frase = list(input('Digite uma expressão: '))

count = 0
for x in frase:
    if x == '(':
        count+=1

    elif x == ')':
        
        if count >= 1:
            count-=1
        else:
            count+=1

print(count)
