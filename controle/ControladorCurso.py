from limite.TelaCurso import TelaCurso
from entidade.curso import Curso
from controle.ControladorAula import ControladorAula
from limite.TelaAula import TelaAula

class ControladorCurso():
  def __init__(self, controlador_sistema):
    #self.__cursos = [nome, descricao, qtdhoras, lista_conteudos]
    self.__cursos = []
    self.__tela_curso = TelaCurso()
    self.__controlador_sistema = controlador_sistema
    self.__controlador_aula = ControladorAula(self)

  def pega_curso_por_nome(self, nome: str):
    for curso in self.__cursos:
      if (curso.nome_do_curso == nome):
        return curso
    return None

  def adiciona_conteudo_curso(self, curso, conteudo):
    curso.adicionar_aula(conteudo)

  def incluir_curso(self):
    dados_curso = self.__tela_curso.pega_dados_curso()
    curso = Curso(dados_curso["nome_do_curso"], dados_curso["descricao"], 
                    dados_curso["quantidade_horas"], dados_curso["lista_conteudos"])
    self.__cursos.append(curso)

  def lista_cursos(self):
    if len(self.__cursos) == 0:
      print("Lista de cursos está vazia")

    for curso in self.__cursos:
      self.__tela_curso.mostra_curso({"nome_do_curso": curso.nome_do_curso, 
        "descricao": curso.descricao, "quantidade_horas": curso.quantidade_horas})

  def alterar_curso(self):
    self.__tela_curso.mostra_mensagem("Alterar curso \n")

    #self.lista_cursos()
    nome_do_curso = self.__tela_curso.seleciona_curso()
    curso = self.pega_curso_por_nome(nome_do_curso)

    if (curso != None):
      novos_dados_curso = self.__tela_curso.pega_dados_curso()
      curso.nome_do_curso = novos_dados_curso["nome_do_curso"]
      curso.descricao = novos_dados_curso["descricao"]
      curso.quantidade_horas = novos_dados_curso["quantidade_horas"]
      self.lista_cursos()

    else:
      self.__tela_curso.mostra_mensagem("ATENÇÃO!!! Curso inexistente")

  def lista_cursos(self):
    if len(self.__cursos) == 0:
      print("Lista de cursos está vazia")

    for curso in self.__cursos:
      self.__tela_curso.mostra_curso({"nome_do_curso": curso.nome_do_curso, 
        "descricao": curso.descricao, "quantidade_horas": curso.quantidade_horas})

  def excluir_curso(self):
    self.lista_cursos()
    nome_do_curso = self.__tela_curso.seleciona_curso()
    curso = self.pega_curso_por_nome(nome_do_curso)

    if (curso != None):
      self.__cursos.remove(curso)
      self.lista_cursos()
    else:
      self.__tela_curso.mostra_mensagem("ATENÇÃO!!! Curso inexistente")

  def abre_aula(self):
    self.__controlador_aula.abre_tela()

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_curso, 2: self.alterar_curso, 
      3: self.lista_cursos, 4: self.excluir_curso, 5:self.abre_aula, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_curso.tela_opcoes()]()
  
  def mostra_conteudo(self):
    lista_opcoes = {1: 'self.lista_conteudos', 2:'self.adicionar_conteudo', 3: 'self.editar_conteudo', 
      4: 'self.remover_conteudo', 0: self.abre_tela}

    continua = True
    while continua:
      lista_opcoes[self.__tela_curso.mostra_curso()]()