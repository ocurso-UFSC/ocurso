from limite.telaCurso import TelaCurso
from entidade.curso import Curso

class ControladorCurso():
  def __init__(self, controlador_sistema):
    #self.__cursos = [nome, descricao, qtdhoras, lista_conteudos]
    self.__cursos = []
    self.__tela_curso = TelaCurso()
    self.__controlador_sistema = controlador_sistema

  
  @property
  def cursos(self):
    return self.__cursos

  @property
  def lista_cursos(self):
    return self.__cursos

  def lista_cursos(self):
    lista_cursos = self.__cursos
    return lista_cursos

  def pega_curso_por_nome(self, nome: str):
    for curso in self.__cursos:
      if (curso.nome_do_curso == nome):
        return curso
    return None

  def incluir_curso(self):
    dados_curso = self.__tela_curso.pega_dados_curso()
    curso = Curso(dados_curso["nome_do_curso"], dados_curso["descricao"], 
                    dados_curso["quantidade_horas"])
    self.__cursos.append(curso)

  def lista_cursos(self):
    if len(self.__cursos) == 0:
      self.__tela_curso.mostra_mensagem("Lista de cursos está vazia")

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
      self.__tela_curso.mostra_mensagem("Lista de cursos está vazia")

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
    
  def abre_aulas(self):
    self.__controlador_sistema.abre_aulas()

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_curso, 2: self.alterar_curso, 
      3: self.lista_cursos, 4: self.excluir_curso, 5:self.abre_aulas, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_curso.tela_opcoes()]()
