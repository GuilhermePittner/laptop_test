import random

lista = []


for i in range(0,5):

    """
    Caso queira input do usuário, descomentar a linha 11 e comentar a linha 12.
    """
    #number = int(input('Digite um valor: '))
    number = random.randint(0,1000)

    if len(lista) == 0:
        lista.append(number)

    else:

        for y,x in enumerate(lista):
    
            if number < x:
                lista.insert(y, number)
                break
            else:
                lista.append(number)
                lista.sort()
                break
                
print(lista)