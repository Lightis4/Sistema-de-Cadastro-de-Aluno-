from dados import alunos


def editar_aluno():
    if not alunos:
        print("\nNenhum aluno cadastrado.")
        return

    print("\n===== ALUNOS CADASTRADOS =====")

    for i, aluno in enumerate(alunos, start=1):
        print(f"{i} - {aluno['nome']}")

    try:
        numero = int(input("\nDigite o número do aluno que deseja editar: "))
    except ValueError:
        print("\nDigite apenas um número.")
        return

    if numero < 1 or numero > len(alunos):
        print("\nAluno não encontrado.")
        return

    aluno = alunos[numero - 1]

    print("\n===== NOVOS DADOS =====")

    novo_nome = input("Nome: ")

    try:
        nova_idade = int(input("Idade: "))
    except ValueError:
        print("\nA idade deve ser um número.")
        return

    novo_curso = input("Curso: ")

    aluno["nome"] = novo_nome
    aluno["idade"] = nova_idade
    aluno["curso"] = novo_curso

    print("\nAluno atualizado com sucesso!")