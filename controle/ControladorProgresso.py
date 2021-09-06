from limite.TelaProgresso import TelaProgresso
from entidade.progresso import Progresso

class ControladorProgresso():
  def __init__(self, controlador_sistema):
    self.__progressos = []
    self.__tela_progresso = TelaProgresso()
    self.__controlador_sistema = controlador_sistema

  def cria_progresso(self, usuario, curso):
    progresso = Progresso(usuario, curso)
    self.adiciona_progresso(progresso)
    return True

  def adiciona_progresso(self, progresso):
    self.__progressos.append(progresso)
    return True

  def assisti_aula(self, progresso, aula):
    progresso.aulas_conconluidas[aula-1] = True
    return True

  def dar_nota(self, progresso, nota):
    progresso.nota = nota

  def todos_progressos_por_usuario(self, usuario):
    progressos = []
    for progresso in self.__progressos:
      if progresso.usuario == usuario:
        progressos.append(progresso)
    return progressos

  def mostra_relatorio_indv(self, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado

    self.__tela_progresso.mostra_mensagem("\nUsuário: {}" .format(usuario.nome))

    prog = self.todos_progressos_por_usuario(usuario)
    
    if len(prog) != 0:
      for progresso in prog:
        self.__tela_progresso.mostra_mensagem("Curso: {}".format(progresso.curso.nome_do_curso))
        
        if progresso.nota != None:
          self.__tela_progresso.mostra_mensagem("Nota: {}".format(progresso.nota))
        else:
          self.__tela_progresso.mostra_mensagem("Sem nota cadastrada")
    
    else:
      print('Nenhum progresso encontrado')

  def mostra_relatorio_todos(self):
    usuarios = self.__controlador_sistema.controlador_usuario.usuarios
    for usuario in usuarios:
      self.mostra_relatorio_indv(usuario)

  def gerar_certificado(self):
    return ("Usuario", self.usuario.nome, "Completou o curso", self.curso.nome_do_curso,
            "com uma carga horária de ", self.curso.quantidade_horas)

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.mostra_relatorio_indv, 2: self.mostra_relatorio_todos, 3: self.gerar_certificado, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_progresso.tela_opcoes()]()