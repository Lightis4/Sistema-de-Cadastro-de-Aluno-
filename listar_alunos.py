def listar_alunos ():
 
  if not alunos:
   print("nemhum_aluno_cadastrado")
  return 
print ("alunos cadastrados")
for i, aluno in enumerate (alunos, start=1):
              
 print(f"aluno{i}")
 print(f"nome: {aluno['nome']}")
 print(f"idade: {aluno['idade']}") 
 print(f"curso: {aluno['curso']}")
 print(f"matricula: {aluno['matricula']}")

