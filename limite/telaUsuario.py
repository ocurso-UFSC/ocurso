
class TelaUsuario():
  def tela_opcoes(self):
    print("Escolha uma das opções a seguir")
    entrada = input(
      '''
      1 - Adicionar Usuário
      2 - Alterar Usuário 
      3 - Listar Usuários
      4 - Excluir Usuário
      '''
    )

    return entrada

  def pega_dados_usuario(self):
    print("Entre com os dados do usuário: ")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
  
    return {"nome": nome, "email": email, "senha": senha}


  def mostra_usuario(self, dados_usuario):
    print("Nome: ", dados_usuario["nome"])
    print("Email: ", dados_usuario["email"])
    print("Senha: ", dados_usuario["senha"])
    print()

  def seleciona_usuario(self):
    email = input("Qual o o email do usuario deseja buscar? ")
    return email

  def mostra_mensagem(self, msg):
    print(msg)