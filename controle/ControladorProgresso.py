from limite.TelaProgresso import TelaProgresso
from entidade.progresso import Progresso

class ControladorProgresso():
  def __init__(self, controlador_sistema):
    self.__progressos = []
    self.__tela_progresso = TelaProgresso()
    self.__controlador_sistema = controlador_sistema

  def cria_progresso(self, usuario, curso):
    progresso = Progresso(usuario, curso)
    self.__progressos.append(progresso)
    return True

  def adiciona_progresso(self, progresso):
    self.__progressos.append(progresso)
    return True

  def assisti_aula(self, progresso, aula):
    progresso.aulas_conconluidas[aula-1] = True
    return True

  def dar_nota(self, progresso, nota):
    progresso.nota = nota

  
  def todos_progressos_por_nome(self, nome):
    progressos = []
    
    for progresso in self.__progressos:
      if progresso.usuario.nome == nome:
        progressos.append(progresso)
    
    return progressos

  def mostra_relatorio_indv(self):
    pass

  def mostra_relatorio_todos(self):
    pass

  def gerar_certificado(self):
    return ("Usuario", self.usuario.nome, "Completou o curso", self.curso.nome_do_curso,
            "com uma carga horária de ", self.curso.quantidade_horas)

  def abre_tela(self):
    lista_opcoes = {1: self.mostra_relatorio_indv, 2: self.mostra_relatorio_todos}

    continua = True
    while continua:
      lista_opcoes[self.__tela_progresso.tela_opcoes()]()