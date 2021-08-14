
class TelaProgresso():
  def tela_opcoes(self):
    print("Escolha uma das opções a seguir")
    entrada = input(
      '''
      1 - Visualizar progresso
      2 - Gerar certificado
      '''
    )

    return entrada

  def pega_dados_usuario(self):
    print("Entre com os dados do usuário: ")
    email = input("Email: ")

    return {"email": email}

  def mostra_mensagem(self, msg):
    print(msg)