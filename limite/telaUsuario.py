class TelaUsuario():
  def tela_opcoes_adm(self):
    entrada = int(input(
'''
---------- Usuario  ----------
Escolha uma das opções a seguir
1 - Minhas informações
2 - Listar todos usuários
3 - Alterar meus dados
4 - Cadastrar Usuário
5 - Alterar Usuário 
6 - Excluir Usuário
7 - Excluir a minha conta
0 - Voltar

Escolha a opção: '''))

    return entrada

  def tela_opcoes(self):
    entrada = int(input(
'''
---------- Usuario  ----------
Escolha uma das opções a seguir
1 - Minhas informações
2 - Alterar minhas informações
3 - Excluir a minha conta
0 - Voltar

Escolha a opção: '''))

    return entrada

  def pega_dados_usuario(self):
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    adm = input("Adm? s/Sim n/Nao: ")
  
    return {"nome": nome, "email": email, "senha": senha, "adm": adm}

  def pega_login(self):
    print("Entre com login do usuário: ")
    email = input("Email: ")
    senha = input("Senha: ")
  
    return {"email": email, "senha": senha}

  def mostra_usuario(self, usuario):
    print("Nome: ", usuario.nome)
    print("Email: ", usuario.email)
    print("Senha: ", usuario.senha)
    print("ADM: ", usuario.adm, '\n')

  def seleciona_usuario(self):
    email = input("Qual o o email do usuario deseja buscar? ")
    return email

  def mostra_mensagem(self, msg):
    print(msg)