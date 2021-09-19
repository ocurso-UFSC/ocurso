import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

class TelaProgresso():
  def __init__(self):
    self.__window = None
    self.__window2 = None
  
  @property
  def window(self):
    return self.__window

  def init_components(self, adm):
    sg.ChangeLookAndFeel('DarkBlue')

    botao_1 = [[sg.Button('Meu relatório', size=(20,2), key=1)]]
    botao_adm = [[sg.Button('Todos Usuários', size=(20,2), key=2)]]
    botao_2 = [[sg.Button('Voltar', size=(20,2), key=0)]]

    if adm:
      botoes = botao_1 + botao_adm + botao_2
    
    else:
      botoes = botao_1 + botao_2

    layout = [
      [sg.Text('Usuário - oCurso', size=(15,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window = sg.Window("Progresso", default_element_size=(40, 1)).Layout(layout)

  def open(self, adm):
    self.init_components(adm)
    button, values = self.__window.Read()
    return button

  def close(self):
    if self.__window != None:
      self.__window.Close()
    self.__window = None


  def listar_todos_usuarios(self, lista_usuarios):
    botoes = [[sg.Button("Selecionar", key=1), sg.Button("Sair", key=0)]]
    layout = [
      [sg.Text('Todos Usuários', size=(15, 1), font=("Helvetica", 15))],
      [sg.Listbox(values=lista_usuarios, key="email", size=(20, 10))],
      [sg.Column(botoes, justification='center', k='-C-')],
    ]

    self.__window2 = sg.Window("Escolha o Usuário", default_element_size=(100, 1)).Layout(layout)

  def cursos_cadastrados_usuario(self, lista_cursos):
    botoes = [[sg.Button("Selecionar", key=1), sg.Button("Sair", key=0)]]
    layout = [
      [sg.Text('Selecione o Curso', size=(15, 1), font=("Helvetica", 15))],
      [sg.Listbox(values=lista_cursos, key="nome_curso", size=(20, 10))],
      [sg.Column(botoes, justification='center', k='-C-')],
    ]

    self.__window2 = sg.Window("Cursos", default_element_size=(100, 1)).Layout(layout)

  def detalhes_progresso(self, dados_progresso):
    botoes = [[sg.Button("Emitir Certificado", key=1), sg.Button("Sair", key=0)]]

    infos = [
      [sg.Text('Aluno', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_progresso["nome_aluno"], font=("Helvetica", 15))],
      [sg.Text('Curso', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_progresso["nome_curso"], font=("Helvetica", 15))],
      [sg.Text('Aulas Concluidas', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text((str(dados_progresso["aula_concluida"]) + "%"), font=("Helvetica", 15))], 
      [sg.Text('Nota', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(dados_progresso["nota"], font=("Helvetica", 15))],
      ]

    layout = [[sg.Text('Informações', size=(15,1), font=("Helvetica", 25), justification='center')],
              [sg.Column(infos, justification='center')],
              [sg.Column(botoes, justification='center', k='-C-')],
    ]

    self.__window2 = sg.Window("Informações", default_element_size=(40, 1)).Layout(layout)

  def open_opcao(self, opcao, dados = None): #dados eh opcional
    if opcao == 1:
      self.cursos_cadastrados_usuario(dados)

    elif opcao == 2:
      self.detalhes_progresso(dados)

    elif opcao == 3: 
      self.listar_todos_usuarios(dados)

    button, values = self.__window2.Read()
    return button, values

  def close_opcao(self):
    if self.__window2 != None:
      self.__window2.Close()
    self.__window2 = None

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup(titulo, mensagem)