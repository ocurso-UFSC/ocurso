import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

class TelaUsuario():
  def __init__(self):
    self.__window = None
    self.__window2 = None

  @property
  def window(self):
    return self.__window

  def init_components(self, adm):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes_1 = [[sg.Button('Minhas Informações', size=(20,2), key=1)]]
    botoes_adm = [
        [sg.Button('Listar Todos Usuários', size=(20,2), key=2)],
        [sg.Button('Cadastrar Usuário', size=(20,2), key=3)]
      ]
    botoes_2 = [[sg.Button('Voltar', size=(20,2), key=0)]]

    if adm:
      botoes = botoes_1 + botoes_adm + botoes_2

    else:
      botoes = botoes_1 + botoes_2

    layout = [
      [sg.Text('Usuário - oCurso', size=(15,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(botoes, vertical_alignment='center', justification='center')], 
    ]

    
    self.__window = sg.Window("Usuário", default_element_size=(40, 1)).Layout(layout)

  def open(self, adm):
    self.init_components(adm)
    button, values = self.__window.Read()
    return button

  def close(self):
    if self.__window != None:
      self.__window.Close()
    self.__window = None

  def pega_dados_cadastro(self):
    sg.ChangeLookAndFeel('DarkBlue')

    entrada = [
              [sg.Text("Usuário")],
              [sg.Input(size=(20,2), key="nome")],
              [sg.Text("Email")],
              [sg.InputText(size=(20,2), key="email")],
              [sg.Text("Senha")],
              [sg.InputText(size=(20,2), key="senha")],
              [sg.Text("Repita a senha")],
              [sg.InputText(size=(20,2), key="senha2")],
              [sg.Button("Salvar", key = 1), sg.Button("Voltar", key = 0)]
            ]

    layout = [
      [sg.Text('Cadastro', size=(10,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window2 = sg.Window("Cadastro", default_element_size=(30, 1)).Layout(layout)

  def mostra_info_usuario(self, dados_usuario):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes = [[sg.Button("Editar", key=1), sg.Button("Excluir", key=2), sg.Button("Sair", key=0)]]

    infos = [
      [sg.Text('Email', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_usuario["email"], font=("Helvetica", 15))],
      [sg.Text('Nome', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_usuario["nome"], font=("Helvetica", 15))],
      [sg.Text('Senha', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_usuario["senha"], font=("Helvetica", 15))], 
      [sg.Text('ADM', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_usuario["adm"], font=("Helvetica", 15))],
      ]

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
  
  def edita_usuario(self, dados_usuario, adm): # adm is boolean
    botoes = [[sg.Button("Salvar", key=1), sg.Button("Sair", key=0)]]

    infos = [
      [sg.Text('Email', size=(8, 1), font=("Helvetica", 15)),
        sg.Text(dados_usuario["email"], key="email")],

      [sg.Text('Usuario', size=(8, 1), font=("Helvetica", 15)),
        sg.InputText(dados_usuario["nome"], key="nome")],

      [sg.Text('Senha', size=(8, 1), font=("Helvetica", 15)),
        sg.InputText(dados_usuario["senha"], key="senha")],        
      ]

    if adm:
      infos.extend([
        [sg.Text('ADM', size=(8, 1), font=("Helvetica", 15)),
        sg.Radio('Sim', "radio", key="adm", default = dados_usuario["adm"]),
        sg.Radio('Não', "radio", key="n_adm", default = (not dados_usuario["adm"]))]
        ])

    layout = [[sg.Text('Informações', size=(15,1), font=("Helvetica", 25), justification='center')],
              [sg.Column(infos, justification='center')],
              [sg.Column(botoes, justification='center', k='-C-')],
            ]

    self.__window2 = sg.Window("Informações", default_element_size=(40, 1)).Layout(layout)

  def open_edit_user(self, dados, adm):
    self.edita_usuario(dados, adm)
    button, values = self.__window2.Read()
    print (button, values)
    
    return button, values

  def open_opcao(self, opcao, dados = None): #dados eh opcional
    if opcao == 1:
      self.mostra_info_usuario(dados)

    elif opcao == 2: 
      self.listar_todos_usuarios_info(dados)

    elif opcao == 3:
      self.pega_dados_cadastro()

    button, values = self.__window2.Read()
    print (button, values)
    return button, values

  def close_opcao(self):
    self.__window2.Close()
    self.__window2 = None

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup(titulo, mensagem)