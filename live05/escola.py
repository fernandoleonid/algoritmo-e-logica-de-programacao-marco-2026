# Responsabilidade única
# Funções puras

def calcularMedia(a, b):
    return (a + b) / 2

def verificarSituacao (media):
    if media >= 5:
        return 'Aprovado'
    else:
        return 'Reprovado'

def calcularMediaTurma (medias):
    soma = 0
    quantidade = len(medias)
    for media in medias:
        soma += media
    
    return soma / quantidade 