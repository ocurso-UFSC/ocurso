import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button


class TelaCurso():

  def __init__(self):
    self.__window = None
    self.__window2 = None

  def init_components(self, adm):

    botao_1 = [[sg.Button('Listar Cursos', size=(20,2), key=1)]]
    botao_adm = [[sg.Button('Cadastrar Curso', size=(20,2), key=2)]]
    botao_2 = [[sg.Button('Voltar', size=(20,2), key=0)]]

    if adm:
      botoes = botao_1 + botao_adm + botao_2

    else:
      botoes = botao_1 + botao_2

    layout = [
      [sg.Text('Cursos - oCurso', size=(15,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window = sg.Window("Cursos", default_element_size=(40, 1)).Layout(layout)

  def open(self, adm):
    self.init_components(adm)
    button, values = self.__window.Read()
    return button

  def close(self):
    if self.__window != None:
      self.__window.Close()
    self.__window = None


  def listar_todos_cursos_info(self, lista_cursos):
    botoes = [[sg.Button("Selecionar", key=1), sg.Button("Sair", key=0)]]
    layout = [
      [sg.Text('Todos Cursos', size=(15, 1), font=("Helvetica", 15))],
      [sg.Listbox(values=lista_cursos, key="nome_curso", size=(20, 10))],
      [sg.Column(botoes, justification='center', k='-C-')],
    ]

    self.__window2 = sg.Window("Cursos", default_element_size=(100, 1)).Layout(layout)

  def detalhe_curso(self, infos_curso, cadastrado, adm):
    if cadastrado:
      botoes = [[sg.Button("Aulas", key= 1), sg.Button("Avaliação", key=2), sg.Button("Sair", key=0)]]
    else:
      botoes = [[sg.Button("Cadastrar", key=9), sg.Button("Sair", key=0)]]
    botoes_adm = [[sg.Button("Editar Curso", key=3), sg.Button("Excluir Curso", key=4)]]

    if adm:
      botoes.extend(botoes_adm)

    infos = [
      [sg.Text('Nome', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(infos_curso["nome_curso"], font=("Helvetica", 15))],

      [sg.Text('Descricao', size=(8, 1), font=("Helvetica", 15))],
      [sg.Multiline(default_text=infos_curso["descricao"], size=(35, 3))],

      [sg.Text('Horas', size=(8, 1), font=("Helvetica", 15)), 
        sg.Text(infos_curso["horas"], font=("Helvetica", 15))], 
      ]

    layout = [[sg.Text('Curso', size=(15,1), font=("Helvetica", 25), justification='center')],
              [sg.Column(infos, justification='center')],
              [sg.Column(botoes, justification='center')],
    ]

    self.__window2 = sg.Window("Curso", default_element_size=(40, 1)).Layout(layout)

  def lista_cursos_info(self, lista_usuarios):
    botoes = [[sg.Button("Editar", key=1), sg.Button("Sair", key=0)]]
    layout = [
      [sg.Text('Todos Usuários', size=(15, 1), font=("Helvetica", 15))],
      [sg.Listbox(values=lista_usuarios, key="nome_curso", size=(20, 10))],
      [sg.Column(botoes, justification='center', k='-C-')],
    ]

    self.__window2 = sg.Window("Informações", default_element_size=(100, 1)).Layout(layout)


  def alterar_curso(self, dados_antigos):
    # tambem serve para alterar curso, caso receber dados
    horas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    entrada = [
              [sg.Text("Nome")],
              [sg.Input(size=(20,2), default_text= dados_antigos['nome_curso'], key="nome_curso")],
              [sg.Text("Descricao")],
              [sg.Multiline(key="descricao", default_text= dados_antigos['descricao'], size=(35, 3))],
              [sg.Text("Qnt. Horas"),
                sg.Spin(values=horas, size=(5, 5), initial_value= dados_antigos['horas'], key="horas")],
              [sg.Button("Salvar", key = 1), sg.Button("Voltar", key = 0)]
            ]

    layout = [
      [sg.Text('Cadastrar Curso', size=(18,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window2 = sg.Window("Cadastro Curso", default_element_size=(50, 1)).Layout(layout)

  def cadastrar_curso(self):
    # tambem serve para alterar curso, caso receber dados
    horas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    entrada = [
              [sg.Text("Nome")],
              [sg.Input(size=(20,2), key="nome_curso")],
              [sg.Text("Descricao")],
              [sg.Multiline(key="descricao", size=(35, 3))],
              [sg.Text("Qnt. Horas"),
                sg.Spin(values=horas, size=(5, 5), key="horas")],
              [sg.Button("Salvar", key = 1), sg.Button("Voltar", key = 0)]
            ]

    layout = [
      [sg.Text('Cadastrar Curso', size=(18,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(entrada, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window2 = sg.Window("Cadastro Curso", default_element_size=(50, 1)).Layout(layout)

  def open_opcao(self, opcao, dados = None, cadastrado = None, adm = None): #dados eh opcional
    if opcao == 1:
      self.listar_todos_cursos_info(dados)

    elif opcao == 2:
      self.detalhe_curso(dados, cadastrado, adm)

    elif opcao == 3:
      self.cadastrar_curso()

    elif opcao == 4:
      self.alterar_curso(dados)

    button, values = self.__window2.Read()
    return button, values

  def close_opcao(self):
    if self.__window2 != None:
      self.__window2.Close()
    self.__window2 = None

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup(titulo, mensagem)
