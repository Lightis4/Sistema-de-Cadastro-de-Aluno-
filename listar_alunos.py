from dados import alunos


def listar_alunos():
    if not alunos:
        print("\nNenhum aluno cadastrado.")
        return

    print("\n===== ALUNOS CADASTRADOS =====")

    for i, aluno in enumerate(alunos, start=1):
        print(f"\nAluno {i}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Matrícula: {aluno['matricula']}")