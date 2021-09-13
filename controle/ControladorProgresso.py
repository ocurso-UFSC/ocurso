from limite.TelaProgresso import TelaProgresso
from entidade.progresso import Progresso

class ControladorProgresso():
  def __init__(self, controlador_sistema):
    self.__progressos = []
    self.__tela_progresso = TelaProgresso()
    self.__controlador_sistema = controlador_sistema

  def cria_progresso(self, curso, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado

    progresso = Progresso(usuario, curso)
    self.adiciona_progresso(progresso)
    return True

  def progresso_por_curso_e_usuario(self, curso, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado
    
    for progresso in self.__progressos:
      if progresso.usuario == usuario and progresso.curso == curso:
        return progresso
    return None
        
  def cadastrar_no_curso(self, usuario = None):
    self.__tela_progresso.mostra_mensagem('Opções de Cursos:')
    self.__controlador_sistema.controlador_curso.lista_cursos()
    self.__tela_progresso.mostra_mensagem("\nEntre com o nome do curso desejado...")
    entrada = self.__tela_progresso.pega_entrada("Nome: ")
    curso = self.__controlador_sistema.controlador_curso.pega_curso_por_nome(entrada)

    if curso != None:
      if self.progresso_por_curso_e_usuario(curso, usuario) != None:
        self.__tela_progresso.mostra_mensagem("Usuário já é cadastrado nesse curso")
      else:
        self.cria_progresso(curso, usuario)
        self.__tela_progresso.mostra_mensagem("Cadastrado no curso com sucesso")
        return True

    else:
      self.__tela_progresso.mostra_mensagem("Curso inexistente")
    
    return False

  def adiciona_progresso(self, progresso):
    self.__progressos.append(progresso)
    return True

  def definir_ultima_aula(self, aula, curso, usuario = None):
    try:
      if usuario == None:
        usuario = self.__controlador_sistema.usuario_logado
      
      progresso = self.progresso_por_curso_e_usuario(curso, usuario)
      progresso.ultima_aula = aula
      return True
    except:
      return False

  def pegar_ultima_aula(self, curso, usuario = None):
    try:
      if usuario == None:
        usuario = self.__controlador_sistema.usuario_logado
      
      progresso = self.progresso_por_curso_e_usuario(curso, usuario)
      return progresso.ultima_aula
    
    except:
      return None

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
        self.__tela_progresso.mostra_mensagem("\nCurso: {}".format(progresso.curso.nome_do_curso))
        ptg_conc = (progresso.ultima_aula / len(progresso.curso.lista_aulas)) * 100
        self.__tela_progresso.mostra_mensagem("Concluiu: {} ptg  das aulas".format(ptg_conc))
        
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
    # nome_curso = 
    return ("Usuario", self.usuario.nome, "Completou o curso", self.curso.nome_do_curso,
            "com uma carga horária de ", self.curso.quantidade_horas)

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_no_curso, 2: self.mostra_relatorio_indv, 3: self.mostra_relatorio_todos, 4: self.gerar_certificado, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_progresso.tela_opcoes()]()