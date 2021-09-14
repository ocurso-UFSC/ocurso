import PySimpleGUI as sg

class TelaLogin():
  def __init__(self):
    self.__window = None
    self.init_components()

  def init_components(self):
    sg.ChangeLookAndFeel("Reddit")

    botoes = [
              [sg.Button('Login', size=(20,2), key=1, button_color='#7B68EE')],
              [sg.Button('Cadastro', size=(20,2), key=2)],
              [sg.Button('Visitante', size=(20,2), key=3)],
              [sg.Button('Sair do sistema', size=(20,2), key=0)]
            ]

    layout = [
      [sg.Text('oCurso', size=(30,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window = sg.Window("Login", default_element_size=(40, 1)).Layout(layout)

  def open(self):
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
    adm = input("ADM? s/sim n/nao: ")
  
    return {"nome": nome, "email": email, "senha": senha, "senha2": senha2, "adm":adm}

  def mostra_mensagem(self, msg):
    print(msg)