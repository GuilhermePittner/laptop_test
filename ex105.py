def notas(*notas, situ=False):
    
    turma = {}
    
    total_notas = 0

    for ind, nota in enumerate(notas):

        if ind == 0:
            maior_nota = menor_nota = nota

        else:

            if nota > maior_nota:
                maior_nota = nota

            if nota < menor_nota:
                menor_nota = nota

        total_notas += nota    
    

    # calculos finais
    media = total_notas/(ind+1)

    turma['total'] = (ind+1)
    turma['maior'] = maior_nota
    turma['menor'] = menor_nota
    turma['média'] = round(media, 2)

    if situ:
        
        if media <= 5:
            situacao = 'RUIM FML'
        
        elif media > 5:
            situacao = 'BOA PAIZAO'
            
        turma['situação'] = situacao


    print(f'Resultados finais: {turma}')


resp = notas(10, 10, 5, 7, 8, 1, 9, 6, 3, 8, 2, situ=True)
resp = notas(1, 1, 5, 7, 1, 1, 1, 6, 3, 8, 2)


# total
# maior
# menor
# media
