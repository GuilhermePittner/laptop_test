frase = str(input('phrase/word please: '))
nfrase = ''

for x in reversed(frase):
    nfrase+=x

if frase.replace(' ','') == nfrase.replace(' ',''): 
    print('palíndromo')
else:
    print('num é')
