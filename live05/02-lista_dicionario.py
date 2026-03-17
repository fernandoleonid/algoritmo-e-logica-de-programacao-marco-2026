turma = [
    {"nome":"Ana", "Idade":"34", "UF":"SP"},
    {"nome":"Pedro", "Idade":"4", "UF":"MG"},
    {"nome":"Hugo", "Idade":"12", "UF":"RJ"}
]

novoAluno = {
    "nome": "Marcelo",
    "Idade": "78"
}

turma.append(novoAluno)

for aluno in turma:
    print (f"{aluno['nome']} - {aluno["Idade"]}")