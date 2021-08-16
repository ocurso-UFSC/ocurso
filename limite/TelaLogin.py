
class TelaLogin():
  def tela_opcoes(self):
    entrada = int(input(
'''
---------- oCurso  ------------
Escolha uma das opções a seguir
1 - Logar
2 - Cadastrar Usuário
3 - AUTOMATICO
0 - Finalizar

Digite a opção: '''))

    return entrada

  def pega_login(self):
    print("Entre com login do usuário: ")
    email = input("Email: ")
    senha = input("Senha: ")
  
    return {"email": email, "senha": senha}

  def pega_dados_cadastro(self):
    print("Cadastrando usuário...")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    senha2 = input("Repita a senha: ")
  
    return {"nome": nome, "email": email, "senha": senha, "senha2": senha2}

  def mostra_mensagem(self, msg):
    print(msg)