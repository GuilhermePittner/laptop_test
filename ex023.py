number = input('Number please ')

valores = ['Unidade', 'Dezena', 'Centena', 'Milhar']    # unit names list

"""
loop user's number and then reverse it
"""
listinha = [x for x in number]
listinha.reverse()

i=0    # index var

"""
loop trough user's reverse number and printing with the units 
"""
for y in listinha:
    print(valores[i],y)
    i+=1