higher = 0
lower = -1

for i in range(0,5):
    weight = int(input('What is your weight? '))
    
    if weight > higher:
        higher = weight

    if weight < lower or lower == -1:
        lower = weight

print('{} was the highest weight.'.format(higher))
print('{} was the lowest weight.'.format(lower))