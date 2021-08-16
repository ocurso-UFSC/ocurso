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
Escolha a opcao: '''))

    return entrada

  def pega_dados_curso(self):
    print("Entre com os dados do curso: ")
    nome_do_curso = input("Nome Curso: ")
    descricao = input("Descricao: ")
    quantidade_horas = input("Quantidade horas: ")
  
    return {"nome_do_curso": nome_do_curso, 
      "descricao": descricao, 
      "quantidade_horas": quantidade_horas,
      "lista_conteudos":[]
    }

  def mostra_curso(self, dados_curso):
    print("Nome do Curso: ", dados_curso["nome_do_curso"])
    print("Descricao: ", dados_curso["descricao"])
    print("Quantidade horas: ", dados_curso["quantidade_horas"])
    print('')
    print('Opção 1 - Mostrar conteúdos do curso')
    print('Opção 2 - Adicionar conteúdo')
    print('Opção 3 - Editar conteúdos')
    print('Opção 4 - Remover conteúdos')
    print('Opção 0 - Voltar')
    opcao = int(input("\nO que você deseja fazer agora?"))
    print()
    return opcao


  def seleciona_curso(self):
    nome_curso = input("Qual o nome do curso deseja buscar? ")
    return nome_curso

  def mostra_mensagem(self, msg):
    print(msg)