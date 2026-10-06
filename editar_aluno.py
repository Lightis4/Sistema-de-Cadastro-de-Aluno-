from dados import alunos

def editar_aluno():
    if not alunos:
        print("\nNenhum aluno cadastrado.")
        return

    listar_alunos_para_edicao()

    numero = int(input("\nDigite o número do aluno que deseja editar: "))

    if numero < 1 or numero > len(alunos):
        print("\nAluno não encontrado.")
        return

    aluno = alunos[numero - 1]

    print("\nDigite os novos dados:")

    novo_nome = input("Nome: ")
    nova_idade = int(input("Idade: "))
    novo_curso = input("Curso: ")

    aluno["nome"] = novo_nome
    aluno["idade"] = nova_idade
    aluno["curso"] = novo_curso

    print("\nAluno atualizado com sucesso!")


def listar_alunos_para_edicao():
    print("\n===== ALUNOS CADASTRADOS =====")

    for i, aluno in enumerate(alunos, start=1):
        print(f"{i} - {aluno['nome']}")