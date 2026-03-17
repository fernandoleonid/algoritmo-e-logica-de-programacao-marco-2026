from escola import *

turma = [
    {"nome":"Ana", "nota1":3, "nota2": 10,"UF":"SP"},
    {"nome":"Pedro", "nota1":7, "nota2": 10,"UF":"MG"},
    {"nome":"Hugo", "nota1":9, "nota2": 5,"UF":"RJ"},
    {"nome":"Felipe", "nota1":0, "nota2": 10,"UF":"MG"}
]

medias = []
for aluno in turma:
    media = calcularMedia(aluno['nota1'], aluno['nota2'])
    medias.append(media)
    situacao = verificarSituacao(media)
    print (f'{aluno["nome"]} - {media} - {situacao}')

mediaTurma = calcularMediaTurma(medias)
print (f'Media da Turma: {mediaTurma}')