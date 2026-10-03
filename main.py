# nessa parte estamos importando todas as funções que estão em pastas separadas para usamos ela somente com a variavel registrada
from cadastro_aluno import cadastrar_aluno
from listar_alunos import listar_alunos
from editar_aluno import editar_aluno
from remover_aluno import remover_aluno

# Implementação do menu 
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

# nessa parte ela serve para garantir que a função main() seja executada somente quando você executar aquele arquivo diretamente.
# fazendo com que nenhuma função seja chamada de forma indevida por conta do import por isso essa linha de codigo só sera usada na main.

if __name__ == "__main__":
    main()
