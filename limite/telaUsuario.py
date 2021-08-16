
class TelaUsuario():
  def tela_opcoes(self):
    entrada = int(input(
'''
---------- Usuario  ----------
Escolha uma das opções a seguir
1 - Minhas informações
2 - Cadastrar Usuário
3 - Alterar Usuário 
4 - Listar Usuários
5 - Excluir Usuário
0 - Voltar

Escolha a opção: '''))

    return entrada

  def pega_dados_usuario(self):
    print("Entre com os dados do usuário: ")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
  
    return {"nome": nome, "email": email, "senha": senha}


  def pega_login(self):
    print("Entre com login do usuário: ")
    email = input("Email: ")
    senha = input("Senha: ")
  
    return {"email": email, "senha": senha}

  def mostra_usuario(self, dados_usuario):
    print("Nome: ", dados_usuario["nome"])
    print("Email: ", dados_usuario["email"])
    print("Senha: ", dados_usuario["senha"])
    print("ADM: ", dados_usuario["adm"])
    print()

  def seleciona_usuario(self):
    email = input("Qual o o email do usuario deseja buscar? ")
    return email

  def mostra_mensagem(self, msg):
    print(msg)