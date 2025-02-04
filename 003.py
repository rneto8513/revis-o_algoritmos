# crie um dicionario chamado "aluno" que represente um estudante com as seguintes informações
# nome, idade, curso, notas(uma lista de notas)
alunos = {
    "nome" : "Raimundo",
    "idade" : 19,
    "curso" : "ciencia da computação",
    "notas" :  [7.7, 8.2, 6.6]
}
def exibir_aluno(aluno):
    print(f"nome: {alunos["nome"]}")
    print(f"idade: {alunos["idade"]}")
    print(f"curso: {alunos["curso"]} ")
    print(f"notas: {alunos["notas"]}")
print(exibir_aluno(alunos))

