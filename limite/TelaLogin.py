import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

class TelaLogin():
  def __init__(self):
    self.__window = None
    self.__window2 = None
    self.__window3 = None

  def init_components(self):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes = [
              [sg.Button('Login', size=(20,2), key=1)],
              [sg.Button('Cadastro', size=(20,2), key=2)],
              [sg.Button('Visitante', size=(20,2), key=3)],
              [sg.Button('Sair do sistema', size=(20,2), key=0)]
            ]

    layout = [
      [sg.Text('oCurso', size=(10,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window = sg.Window("Login", default_element_size=(40, 1)).Layout(layout)

  def open(self):
    self.__window = None
    self.init_components()
    button, values = self.__window.Read()
    return button

  def close(self):
    self.__window.Close()

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup(titulo, mensagem)

  def tela_opcoes(self):
    entrada = int(input(
'''
---------- oCurso  ------------
Escolha uma das opções a seguir
1 - Logar
2 - Cadastrar Usuário
3 - Visitante
0 - Finalizar
Digite a opção: '''))

    return entrada

  def pega_login(self):
    sg.ChangeLookAndFeel('DarkBlue')

    entrada = [
              [sg.Text("Email")],
              [sg.InputText(size=(20,2), key="email")],
              [sg.Text("Senha")],
              [sg.InputText(size=(20,2), key="senha")],
              [sg.Button("Entrar")]
            ]

    layout = [
      [sg.Text('Login', size=(10,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window3 = sg.Window("Login", default_element_size=(30, 1)).Layout(layout)

  
  def open_login(self):
    self.pega_login()
    button, values = self.__window3.Read()
    return values

  def close_login(self):
    self.__window3.Close()

  def mostra_mensagem(self, msg):
    print(msg)