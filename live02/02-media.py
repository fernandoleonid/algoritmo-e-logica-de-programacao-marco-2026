nota_prova = float(input('Digite a nota da prova: '))
nota_trabalho = float(input('Digite a nota do trabalho: '))

media = (nota_prova + nota_trabalho) / 2

if media >= 7:
    print ('Aprovado')
elif media >= 5:
    print ('Recuperação')
else:
    print ('Reprovado')
