from cadastro_aluno import cadastrar_aluno
from listar_alunos import listar_alunos
from remover_aluno import remover_aluno

while True:
    print("\n=== SISTEMA ESCOLAR ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Remover aluno")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        remover_aluno()

    elif opcao == "0":
        break