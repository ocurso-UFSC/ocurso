from limite.TelaAula import TelaAula
from entidade.aula import Aula
from controle.ControladorCurso import ControladorCurso
from entidade.curso import Curso

class ControladorAula():
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__tela_aula = TelaAula()
    self.__aula = Aula
    self.__curso = Curso
    self.__controlador_curso = ControladorCurso

  def mostra_aulas(self):
    nome_curso = self.__tela_aula.nome_curso()
    cursos = self.__controlador_sistema.controlador_curso.lista_cursos
    curso = cursos[nome_curso]
    for aula in curso._Curso__lista_aulas:
      self.__tela_aula.mostra_aulas(aula._Aula__descricao, aula._Aula__link_aula)
  
  def adiciona_aula(self):
    nome_curso = self.__tela_aula.nome_curso()
    cursos = self.__controlador_curso.lista_cursos
    dados_aula = self.__tela_aula.pega_dados_aula()
    descricao_aula = dados_aula['descricao_aula']
    link_aula = dados_aula['link_aula']
    aula = self.__aula(descricao_aula, link_aula)
    curso = cursos[nome_curso]
    curso._Curso__lista_aulas.append(aula)
  
  def altera_aula():
    ...
  
  def exclui_aula():
    ...
  
  def retornar(self):
      self.__controlador_sistema.abre_tela()
  
  def abre_tela(self):
      lista_opcoes = {1:self.mostra_aulas, 2:self.adiciona_aula, 3:self.altera_aula, 4:self.exclui_aula, 0:self.retornar}
      continua = True
      while continua:
        lista_opcoes[self.__tela_aula.tela_opcoes()]()
