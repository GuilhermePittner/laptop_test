percurso = float(input('Rodou quantos Km? '))
dias = int(input('Por quantos dias você ficou com o carro? '))

pagar = (dias * 60) + (percurso * 0.15)

print(f'Você percorreu {percurso}Km tendo o carro por {dias} dias, o total a pagar é de R${pagar}')