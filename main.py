
from cadastro_aluno import cadastrar_aluno
from listar_alunos import listar_alunos
from editar_aluno import editar_aluno
from remover_aluno import remover_aluno


def main():
    while True:
        print("\n=== SISTEMA DE CADASTRO DE ALUNOS ===")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Editar aluno")
        print("4 - Remover aluno")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            editar_aluno()

        elif opcao == "4":
            remover_aluno()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()