import PySimpleGUI as sg

class TelaLogin():
  def __init__(self):
    self.__window = None
    self.init_components()

  def init_components(self):
    sg.ChangeLookAndFeel("Reddit")
    coluna1 = [
      [sg.Text('Coluna1', background_color='#d3dfda', justification='center', size=(10,1))],
      [sg.Spin(values=('1', '2', '3'), initial_value='selecione', key='so_spin1')],
      [sg.Spin(values=('1', '2', '3'), initial_value='selecione', key='so_spin2')],
      [sg.Spin(values=('1', '2', '3'), initial_value='selecione', key='so_spin3')]
    ]

    layout = [
      [sg.Text('Teste de TEXTo', size=(30,1), font=("Helvetica", 25))],
      [sg.Text("RESPONDA seu VAGABUNDO")],
      # [sg.InputText("qual seu nome", key="it_nome")],
      # [sg.InputText("qual sua senha", key="it_senha")],
      # [sg.Column(coluna1, background_color='#d3dfda')],
      # [sg.Button('Gravar'), sg.Cancel('Cancelar')]
      [sg.Button('Login', key=1)],
      [sg.Button('Cadastro', key=2)],
      [sg.Button('Visitante', key=3)],
      [sg.Button('Sair', key=0)],

    ]

    self.__window = sg.Window("Titulo", default_element_size=(40, 1)).Layout(layout)

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