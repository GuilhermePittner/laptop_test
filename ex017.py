import math

oposto = float(input('Qual é o tamanho do cateto oposto? (em cm): '))
adjacente = float(input('Qual é o tamanho do cateto adjacente? (em cm): '))

hipotenusa = math.sqrt(oposto*oposto + adjacente*adjacente)
#hipotenusa = math.sqrt((oposto**2) + (adjacente**2))
print(f'Com base nos valores que você me informou (adjacente: {adjacente}cm e oposto: {oposto}cm), a hipotenusa vale {round(hipotenusa,2)}cm')