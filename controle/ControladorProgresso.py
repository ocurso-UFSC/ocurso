from limite.TelaProgresso import TelaProgresso
from entidade.progresso import Progresso

class ControladorCurso():
  def __init__(self, controlador_sistema):
    self.__progressos = []
    self.__tela_curso = TelaProgresso()
    self.__controlador_sistema = controlador_sistema

  def cria_progresso(self, aluno, curso):
    progresso = Progresso(aluno, curso)
    self.__progressos.append(progresso)
    return True

  def assisti_aula(self):
    pass

  def mostra_relatorio_indv(self):
    pass

  def mostra_relatorio_todos(self):
    pass

  def abre_tela(self):
    lista_opcoes = {1: self.assisti_aula, 2: self.mostra_relatorio_indv, 
      3: self.mostra_relatorio_todos}

    continua = True
    while continua:
      lista_opcoes[self.__tela_curso.tela_opcoes()]()
