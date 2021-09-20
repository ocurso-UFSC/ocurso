import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

class TelaLogin():
  def __init__(self):
    self.__window = None
    self.__window2 = None

  def init_components(self):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes = [
              [sg.Button('Login', size=(20,2), key=1)],
              [sg.Button('Cadastro', size=(20,2), key=2)],
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
    if self.__window != None:
      self.__window.Close()
    self.__window = None

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup(titulo, mensagem)

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

    self.__window2 = sg.Window("Login", default_element_size=(30, 1)).Layout(layout)

  def open_login(self):
    self.pega_login()
    button, values = self.__window2.Read()
    return values

  def close_login(self):
    if self.__window2 != None:
      self.__window2.Close()
    self.__window2 = None