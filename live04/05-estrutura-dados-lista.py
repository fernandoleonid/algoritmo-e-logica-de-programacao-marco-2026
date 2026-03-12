alunos = ['Ana', 'Pedro', 'Marta', 'Mario']

print (alunos)

alunos.append('Leonid')
alunos.append('Willian')

print (alunos)

aluno_removido = alunos.pop(1)

print (alunos)

alunos[0] = 'Ana Maria'

print (alunos)

print (alunos.__len__())

print (aluno_removido)