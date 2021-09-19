import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button


class TelaCurso():

  def __init__(self):
    self.__window = None
    self.__window2 = None

  def init_components(self):
    sg.ChangeLookAndFeel('DarkBlue')

    botoes = [
              [sg.Button('Listar Cursos', size=(20,2), key=1)],
              [sg.Button('Cadastrar Curso', size=(20,2), key=2)],
              [sg.Button('Voltar', size=(20,2), key=0)]
    ]

    layout = [
      [sg.Text('Cursos - oCurso', size=(15,1), font=("Helvetica", 25), justification='center')],
      [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]
    ]

    self.__window = sg.Window("Cursos", default_element_size=(40, 1)).Layout(layout)

  def open(self):
    self.init_components()
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

  # def seleciona_curso(self):
  #   nome_curso = input("Qual o nome do curso deseja buscar? ")
  #   return nome_curso

  def detalhe_curso(self, infos_curso):
    botoes = [[sg.Button("Aulas", key=1), sg.Button("Avaliação", key=2), sg.Button("Sair", key=0)]]
    botoes_adm = [[sg.Button("Editar Curso", key=3), sg.Button("Excluir Curso", key=4)]]

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
              [sg.Column(botoes_adm, justification='center')],
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

  def open_opcao(self, opcao, dados = None): #dados eh opcional
    if opcao == 1:
      self.listar_todos_cursos_info(dados)

    elif opcao == 2:
      self.detalhe_curso(dados)

    button, values = self.__window2.Read()
    return button, values

  def close_opcao(self):
    if self.__window2 != None:
      self.__window2.Close()
    self.__window2 = None

  def pega_dados_curso(self):
    print("Entre com os dados do curso: ")
    nome_do_curso = input("Nome Curso: ")
    descricao = input("Descricao: ")
    quantidade_horas = input("Quantidade horas: ")
  
    return {"nome_do_curso": nome_do_curso, 
      "descricao": descricao, 
      "quantidade_horas": quantidade_horas,}

  def mostra_curso(self, dados_curso):
    print("\n")
    print("Nome do Curso: ", dados_curso["nome_do_curso"])
    print("Descricao: ", dados_curso["descricao"])
    print("Quantidade horas: ", dados_curso["quantidade_horas"])


  def mostra_mensagem(self, msg):
    print(msg)

  def show_message(self, titulo: str, mensagem: str):
    sg.Popup(titulo, mensagem)