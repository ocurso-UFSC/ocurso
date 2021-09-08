class TelaCurso():
  def tela_opcoes(self):
    entrada = int(input(
'''
--------- Curso  ---------
Escolha uma das opções a seguir
1 - Adicionar Curso
2 - Alterar Curso 
3 - Listar Curso
4 - Excluir Curso
5 - Aulas
0 - Voltar
Escolha a opcao: '''))

    return entrada

  def pega_dados_curso(self):
    print("Entre com os dados do curso: ")
    nome_do_curso = input("Nome Curso: ")
    descricao = input("Descricao: ")
    quantidade_horas = input("Quantidade horas: ")
  
    return {"nome_do_curso": nome_do_curso, 
      "descricao": descricao, 
      "quantidade_horas": quantidade_horas,}

  def mostra_curso(self, dados_curso):
    print("\n")
    print("Nome do Curso: ", dados_curso["nome_do_curso"])
    print("Descricao: ", dados_curso["descricao"])
    print("Quantidade horas: ", dados_curso["quantidade_horas"])
  
  def ver_aulas(self):
    ...

  def seleciona_curso(self):
    nome_curso = input("Qual o nome do curso deseja buscar? ")
    return nome_curso

  def mostra_mensagem(self, msg):
    print(msg)