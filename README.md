🎓 Sistema de Cadastro de Alunos

Projeto desenvolvido em Python com o objetivo de praticar programação modular, criação de funções, trabalho em equipe e controle de versão utilizando Git e GitHub.

📋 Funcionalidades
Cadastro de alunos
Listagem de alunos
Edição de dados dos alunos
Remoção de alunos
Menu interativo
Compartilhamento de dados entre os módulos

📁 Estrutura do Projeto
Sistema-de-Cadastro-de-Aluno/
│
├── main.py
├── dados.py
├── cadastro_aluno.py
├── listar_alunos.py
├── editar_aluno.py
└── remover_aluno.py

Responsabilidade de cada arquivo
main.py: contém o menu principal e chama as funções de cada módulo.
dados.py: armazena e disponibiliza os dados compartilhados dos alunos.
cadastro_aluno.py: contém as funções responsáveis pelo cadastro.
listar_alunos.py: contém as funções responsáveis pela listagem.
editar_aluno.py: contém as funções responsáveis pela edição.
remover_aluno.py: contém as funções responsáveis pela remoção.

Os módulos serão desenvolvidos separadamente e integrados à branch main por meio de Pull Requests.

🚀 Como executar
1. Clonar o repositório
git clone (https://github.com/Lightis4/Sistema-de-Cadastro-de-Aluno-.git)

2. Entrar na pasta do projeto
cd Sistema-de-Cadastro-de-Aluno

3. Executar o sistema
python main.py

👥 Organização da equipe

A branch main é protegida e representa a versão principal e integrada do projeto.

Cada integrante deve trabalhar em sua própria branch, desenvolver somente a funcionalidade pela qual é responsável e enviar as alterações por Pull Request.

Pedro — Cadastro de alunos 

Branch: feature-cadastro

Arquivo: cadastro_aluno.py

Responsável por implementar o cadastro de novos alunos.

Ronne — Listagem de alunos

Branch: feature-listagem

Arquivo: listar_alunos.py

Responsável por exibir os alunos cadastrados.

Enzo e Carlos — Edição de alunos

Branch: feature-editar

Arquivo: editar_aluno.py

Responsável por permitir a edição dos dados de um aluno cadastrado.

Pedro Barbosa — Remoção de alunos

Branch: feature-remover

Arquivo: remover_aluno.py

Responsável por permitir a remoção de alunos cadastrados.

🔀 Fluxo de trabalho com Git

1. Atualizar as informações do repositório

Antes de começar, execute:

git fetch origin

Esse comando atualiza as referências das branches remotas.

2. Criar a própria branch

Cada integrante deve criar sua branch a partir da main atualizada:

git switch -c nome-da-branch origin/main

Substitua nome-da-branch pelo nome correspondente à sua tarefa.

Exemplo para o responsável pelo cadastro:

git switch -c feature-cadastro origin/main

3. Desenvolver a funcionalidade

O integrante deve implementar e testar o código no arquivo correspondente à sua responsabilidade.

Não devem ser feitas alterações diretamente na branch main.

4. Adicionar as alterações

Para adicionar somente o arquivo desenvolvido:

git add nome-do-arquivo.py

Exemplo:

git add cadastro_aluno.py

5. Criar um commit
git commit -m "Implementa funcionalidade de cadastro"

A mensagem deve descrever de forma clara a alteração realizada.

6. Enviar a branch para o GitHub

git push -u origin nome-da-branch

Exemplo:

git push -u origin feature-cadastro

7. Abrir um Pull Request

Após enviar a branch para o GitHub:

Acessar o repositório.
Abrir a seção Pull requests.
Clicar em New pull request.
Selecionar main como branch de destino (base).
Selecionar a branch do integrante como origem (compare).
Descrever as alterações realizadas.
Solicitar revisão e corrigir eventuais problemas.
Aguardar o cumprimento das regras de proteção.
Após a aprovação, integrar as alterações à main.

🔗 Integração entre os módulos

O main.py será responsável por importar e chamar as funções desenvolvidas nos outros arquivos.

Exemplo ilustrativo:

from cadastro_aluno import cadastrar_aluno
from listar_alunos import listar_alunos

📚 Conceitos utilizados
Import: importa um módulo Python.
From import: importa uma função ou outro elemento específico de um módulo.
Modularização: organiza o programa em arquivos com responsabilidades distintas.
Branches: permitem desenvolver funcionalidades de forma independente.
Commits: registram alterações realizadas no código.
Pull Requests: permitem revisar e integrar alterações.
Merge: integra as alterações de uma branch em outra.


🛠 Tecnologias utilizadas
Python 3
Git
GitHub
PyCharm
