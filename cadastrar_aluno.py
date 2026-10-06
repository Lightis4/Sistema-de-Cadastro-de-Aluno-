from dados import alunos


def cadastrar_aluno():
    print("\n===== CADASTRO DE ALUNO =====")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    matricula = input("Matrícula: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "matricula": matricula
    }

    alunos.append(aluno)

    print(f"\nAluno {nome} cadastrado com sucesso!")