import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

class TelaUsuario():
  def __init__(self):
    self.__window = None
    self.__window2 = None
    self.__window3 = None
    self.init_components()

  def init_components(self):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes = [
              [sg.Button('Minhas Informações', size=(20,2), key=1)],
              [sg.Button('Listar Todos Usuários', size=(20,2), key=2)],
              [sg.Button('Cadastrar Usuário', size=(20,2), key=3)],
              [sg.Button('Alterar Usuário', size=(20,2), key=4)],
              [sg.Button('Excluir Usuário', size=(20,2), key=5)],
              [sg.Button('Excluir a Minha Conta', size=(20,2), key=6)],
              [sg.Button('Sair do Sistema', size=(20,2), key=0)]
    ]

    layout = [
      [sg.Text('Usuário - oCurso', size=(15,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window = sg.Window("Usuário", default_element_size=(40, 1)).Layout(layout)

  def open(self):
    button, values = self.__window.Read()
    return button

  def close(self):
    self.__window.Close()


#   def tela_opcoes(self):
#     entrada = int(input(
# '''
# ---------- Usuario  ----------
# Escolha uma das opções a seguir
# 1 - Minhas informações
# 2 - Alterar minhas informações
# 3 - Excluir a minha conta
# 0 - Voltar

# Escolha a opção: '''))

#     return entrada

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