import math
value = int(input('Qual ângulo deseja calcular? '))

seno = math.sin(math.radians(value))
cosseno = math.cos(math.radians(value))
tangente = math.tan(math.radians(value))

print(f'O seno de {value} é {seno:.2f}')
print(f'O cosseno de {value} é {cosseno:.2f}')
print(f'A tangente de {value} é {tangente:.2f}')


# didn't know about sin/cos/tan methods