import requests

def listar_alunos():
    end_point = 'https://lion-school-phbo.onrender.com/alunos'
    response = requests.get(end_point)
    data = response.json()
    for aluno in data:
        print (f"NOME: {aluno['nome']} - FOTO: {aluno['foto']}")


def listar_cursos():
    end_point = 'https://lion-school-phbo.onrender.com/cursos'
    response = requests.get(end_point)
    data = response.json()
    for curso in data:
        print (f"Curso: {curso['nome']} - SIGLA: {curso['sigla']}")

listar_cursos()