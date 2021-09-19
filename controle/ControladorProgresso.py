from limite.TelaProgresso import TelaProgresso
from entidade.progresso import Progresso
from dao.progresso_dao import progressoDAO

class ControladorProgresso():
  def __init__(self, controlador_sistema):
    self.__dao = progressoDAO()
    # self.__progressos = self.__dao.get_all()
    self.__tela_progresso = TelaProgresso()
    self.__controlador_sistema = controlador_sistema
    self.temporario()

  @property
  def progressos(self):
    return self.__dao.get_all()

  def temporario(self):
    lista_usuarios = list(self.__controlador_sistema.controlador_usuario.usuarios)
    lista_cursos = list(self.__controlador_sistema.controlador_curso.lista_cursos)

    for usuario in lista_usuarios:
      for curso in lista_cursos:
        self.cria_progresso(curso, usuario)

  def get_next_key(self):
    all = self.__dao.get_all()
    return len(all) + 1

  def cria_progresso(self, curso, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado

    codigo = self.get_next_key()
    progresso = Progresso(codigo, usuario, curso)
    
    self.adiciona_progresso(progresso)

    print(self.progressos)
    input("")
    
    return True

  def progresso_por_curso_e_usuario(self, curso, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado

    progressos = self.__dao.get_all()
    for progresso in progressos:
      if progresso.usuario == usuario and progresso.curso == curso:
        return progresso
    return None

  def cursos_ja_cadastrado_por_usuario(self, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado

    lista_cursos = []
    
    progressos = self.__dao.get_all()
    for progresso in progressos:
      if progresso.usuario == usuario:
        lista_cursos.append(progresso.curso.nome_do_curso)
  
    return lista_cursos

  def progresso_to_json(self, progresso):
    dados_progresso = {}
    dados_progresso["nome_aluno"] = progresso.usuario.nome
    dados_progresso["nome_curso"] = progresso.curso.nome_do_curso

    if progresso.nota != None:
      dados_progresso["nota"] = progresso.nota
    else:
      dados_progresso["nota"] = "Sem nota"

    if len(progresso.curso.lista_aulas) != 0:
      ptg_conc = (progresso.ultima_aula / len(progresso.curso.lista_aulas)) * 100
    else:
      ptg_conc = "Nenhuma"
      
    dados_progresso["aula_concluida"] = ptg_conc

    return dados_progresso

  def todos_usuarios(self):
    lista_usuarios_email = []

    progressos = self.__dao.get_all()
    for progresso in progressos:
      if progresso.usuario.email not in lista_usuarios_email:
        lista_usuarios_email.append(progresso.usuario.email)

    while True:

      button, values = self.__tela_progresso.open_opcao(3, lista_usuarios_email)


      if button == 0:
        self.__tela_progresso.close_opcao()
        self.__tela_progresso.close()
        return False

      elif len(values["email"]) == 0:
        self.__tela_progresso.show_message("Erro", "Nenhum selecionado")
        self.__tela_progresso.close_opcao()
        self.__tela_progresso.close()
        return False

      else:
        usuario = self.__controlador_sistema.controlador_usuario.pega_usuario_por_email(values["email"][0])
        self.__tela_progresso.close_opcao()
        self.__tela_progresso.close()
        self.relatorio_ind(usuario)
        # self.informacao_user(usuario)
        return True

  def relatorio_ind(self, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado

    self.__tela_progresso.close()
    lista_cursos = self.cursos_ja_cadastrado_por_usuario(usuario)
    
    while True:
      button, values = self.__tela_progresso.open_opcao(1, lista_cursos)

      if button == 0:
        self.__tela_progresso.close_opcao()
        return False

      elif button == 1: 
        if len(values["nome_curso"]) == 0:
          self.__tela_progresso.show_message("Erro", "Nenhum selecionado")
          self.__tela_progresso.close_opcao()

        else:
          # se estiver ok..
          nome_curso = values["nome_curso"][0]
          curso = self.__controlador_sistema.controlador_curso.pega_curso_por_nome(nome_curso)
          progresso = self.progresso_por_curso_e_usuario(curso, usuario)
          self.__tela_progresso.close_opcao()
          self.detalhes_progresso(progresso)
          return True


  def gerar_certificado(self, progresso):
    if progresso.nota != None:
      self.__tela_progresso.show_message("Parabéns", "Show de bola cara")
      # implementar certificado

    else:
      self.__tela_progresso.show_message("Erro", "Curso não concluído")

  def detalhes_progresso(self, progresso):
    dados_progresso = self.progresso_to_json(progresso)
    button, values = self.__tela_progresso.open_opcao(2, dados_progresso)

    if button == 1:
      self.__tela_progresso.close_opcao()
      self.gerar_certificado(progresso)
      print("Seu certificado...")
      
    else:
      self.__tela_progresso.close_opcao()
        
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
    self.__dao.add(progresso)
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
    progressos_user = []
    progressos = self.__dao.get_all()

    for progresso in progressos:
      if progresso.usuario == usuario:
        progressos_user.append(progresso)

    return progressos_user

  def mostra_relatorio_indv(self, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado

    self.__tela_progresso.mostra_mensagem("\nUsuário: {}" .format(usuario.nome))
    prog = self.todos_progressos_por_usuario(usuario)
    
    if len(prog) != 0:
      for progresso in prog:
        self.__tela_progresso.mostra_mensagem("\nCurso: {}".format(progresso.curso.nome_do_curso))
        
        if len(progresso.curso.lista_aulas) != 0:
          ptg_conc = (progresso.ultima_aula / len(progresso.curso.lista_aulas)) * 100
        else:
          ptg_conc = "NaN"

        self.__tela_progresso.mostra_mensagem("Concluiu: {} ptg  das aulas".format(ptg_conc))
        
        if progresso.nota != None:
          self.__tela_progresso.mostra_mensagem("Nota: {}".format(progresso.nota))
        else:
          self.__tela_progresso.mostra_mensagem("Sem nota cadastrada")
    
    else:
      print('Nenhum progresso encontrado')

  def retornar(self):
    self.__tela_progresso.close()
    self.__tela_progresso.close_opcao()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.relatorio_ind, 2: self.todos_usuarios, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_progresso.open()]()