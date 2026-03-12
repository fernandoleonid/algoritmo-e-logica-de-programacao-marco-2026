notas = [2, 4, 9, 4, 2, 5, 7]

for indice, nota in enumerate(notas):
    if nota >= 5:
        print (f'Aluno {indice} com a nota: {nota} - Aprovado')
    else:
        print (f'Aluno {indice} com a nota: {nota} - Reprovado')