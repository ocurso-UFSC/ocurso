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
              [sg.Button('Voltar', size=(20,2), key=0)]
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
    self.__window = None

  def mostra_info_usuario(self, dados_usuario):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes = [[sg.Button("Editar", key=1), sg.Button("Excluir", key=2), sg.Button("Sair", key=0)]]

    infos = [
      [sg.Text('Usuario', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_usuario["nome"], font=("Helvetica", 15))],
      [sg.Text('Email', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_usuario["email"], font=("Helvetica", 15))],
      [sg.Text('Senha', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_usuario["senha"], font=("Helvetica", 15))], 
      [sg.Text('ADM', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_usuario["adm"], font=("Helvetica", 15))],
      ]
      # [sg.Column(text, vertical_alignment='center', justification='center', k='-C-')]

    layout = [[sg.Text('Informações', size=(15,1), font=("Helvetica", 25), justification='center')],
              [sg.Column(infos, justification='center')],
              [sg.Column(botoes, justification='center', k='-C-')],
    ]

    self.__window2 = sg.Window("Informações", default_element_size=(40, 1)).Layout(layout)


  def listar_todos_usuarios_info(self, lista_usuarios):
    botoes = [[sg.Button("Editar", key=1), sg.Button("Sair", key=0)]]
    layout = [
      [sg.Text('Todos Usuários', size=(15, 1), font=("Helvetica", 15))],
      [sg.Listbox(values=lista_usuarios, key="email", size=(20, 10))],
      [sg.Column(botoes, justification='center', k='-C-')],
    ]

    self.__window2 = sg.Window("Informações", default_element_size=(100, 1)).Layout(layout)
  
  def edita_usuario(self, dados_usuario):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes = [[sg.Button("Salvar", key=1), sg.Button("Sair", key=0)]]

    infos = [
      [sg.Text('Usuario', size=(8, 1), font=("Helvetica", 15)),
        sg.InputText(dados_usuario["nome"], key="nome")],

      [sg.Text('Email', size=(8, 1), font=("Helvetica", 15)),
        sg.InputText(dados_usuario["email"], key="email")],        

      [sg.Text('Senha', size=(8, 1), font=("Helvetica", 15)),
        sg.InputText(dados_usuario["senha"], key="senha")],        

      [sg.Text('ADM', size=(8, 1), font=("Helvetica", 15)),
        sg.Radio('Sim', "radio", key="adm", default = dados_usuario["adm"]), sg.Radio('Não', "radio", key="n_adm", default = (not dados_usuario["adm"]))
      ]]

    layout = [[sg.Text('Informações', size=(15,1), font=("Helvetica", 25), justification='center')],
              [sg.Column(infos, justification='center')],
              [sg.Column(botoes, justification='center', k='-C-')],
            ]

    self.__window2 = sg.Window("Informações", default_element_size=(40, 1)).Layout(layout)

  def open_edit_user(self, dados):
    self.edita_usuario(dados)
    button, values = self.__window2.Read()
    
    return button, values

  def open_opcao(self, opcao, dados = None): #dados eh opcional
    if opcao == 1:
      self.mostra_info_usuario(dados)

    elif opcao == 2: 
      self.listar_todos_usuarios_info(dados)

    button, values = self.__window2.Read()
    return button, values

  def close_opcao(self):
    self.__window2.Close()
    self.__window2 = None

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup(titulo, mensagem)

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