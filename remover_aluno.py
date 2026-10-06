from dados import alunos


def remover_aluno():
    if not alunos:
        print("\nNenhum aluno cadastrado.")
        return

    print("\n===== ALUNOS CADASTRADOS =====")

    for i, aluno in enumerate(alunos, start=1):
        print(f"{i} - {aluno['nome']}")

    try:
        numero = int(input("\nDigite o número do aluno que deseja remover: "))
    except ValueError:
        print("\nDigite apenas um número.")
        return

    if numero < 1 or numero > len(alunos):
        print("\nAluno não encontrado.")
        return

    aluno_removido = alunos.pop(numero - 1)

    print(f"\nAluno {aluno_removido['nome']} removido com sucesso!")