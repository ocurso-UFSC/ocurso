from limite.TelaProgresso import TelaProgresso
from entidade.progresso import Progresso
from dao.progresso_dao import progressoDAO

class ControladorProgresso():
  def __init__(self, controlador_sistema):
    self.__dao = progressoDAO()
    self.__tela_progresso = TelaProgresso()
    self.__controlador_sistema = controlador_sistema
    # self.gera_automatico()

  @property
  def progressos(self):
    return self.__dao.get_all()

  def gera_automatico(self):
    lista_usuarios = list(self.__controlador_sistema.controlador_usuario.usuarios)
    lista_cursos = list(self.__controlador_sistema.controlador_curso.lista_cursos)

    for usuario in lista_usuarios:
      for curso in lista_cursos:
        self.cria_progresso(curso.codigo, usuario.email)

  def get_next_key(self):
    all = list(self.__dao.get_all())
    if len(all) > 0:
      return all[-1].codigo + 1
    else:
      return 1

  def excluir_progresso(self, progresso):
    self.__dao.remove(progresso.codigo)
  
  def excluir_progresso_por_key(self, progresso_codigo):
    self.__dao.remove(progresso_codigo)

  def remove_progresso_por_curso_cod(self, curso_cod):
    lista_progressos = self.__dao.get_all()
    lista_codigos = []

    # salva todos os progressos do curso
    for progresso in lista_progressos:
      if progresso.curso_cod == curso_cod:
        lista_codigos.append(progresso.codigo)

    # apaga eles
    for progresso_codigo in lista_codigos:
      self.excluir_progresso_por_key(progresso_codigo)

  def remove_progresso_por_usuario_cod(self, usuario_cod):
    lista_progressos = self.__dao.get_all()
    lista_codigos = []

    # salva todos os progressos do curso
    for progresso in lista_progressos:
      if progresso.usuario_cod == usuario_cod:
        lista_codigos.append(progresso.codigo)

    # apaga eles
    for progresso_codigo in lista_codigos:
      self.excluir_progresso_por_key(progresso_codigo)
    
  def adiciona_progresso(self, progresso):
    self.__dao.add(progresso)
    return True

  def cria_progresso(self, curso_cod, usuario_cod = None):
    if usuario_cod == None:
      usuario_cod = self.__controlador_sistema.usuario_logado.email

    codigo = self.get_next_key()
    progresso = Progresso(codigo, usuario_cod, curso_cod)
    self.adiciona_progresso(progresso)
    
    return True

  def progresso_por_curso_e_usuario(self, curso_cod, usuario_cod = None):
    if usuario_cod == None:
      usuario_cod = self.__controlador_sistema.usuario_logado.email

    progressos = self.__dao.get_all()
    for progresso in progressos:
      if progresso.usuario_cod == usuario_cod and progresso.curso_cod == curso_cod:
        return progresso
    return None

  def cursos_ja_cadastrado_por_usuario(self, usuario_cod = None):
    if usuario_cod == None:
      usuario_cod = self.__controlador_sistema.usuario_logado.email

    lista_cursos = []
    
    progressos = self.__dao.get_all()
    for progresso in progressos:
      if progresso.usuario_cod == usuario_cod:
        curso = self.__controlador_sistema.controlador_curso.get_curso_por_key(progresso.curso_cod)
        lista_cursos.append(curso.nome_do_curso)
  
    return lista_cursos

  def atualizar_ultima_aula(self, progresso, ultima_aula):
    progresso.ultima_aula = ultima_aula
    self.__dao.update()

  def progresso_to_json(self, progresso):
    dados_progresso = {}

    usuario = self.__controlador_sistema.controlador_usuario.pega_usuario_por_email(progresso.usuario_cod)
    dados_progresso["nome_aluno"] = usuario.nome
    dados_progresso["email"] = usuario.email

    curso = self.__controlador_sistema.controlador_curso.get_curso_por_key(progresso.curso_cod)
    dados_progresso["nome_curso"] = curso.nome_do_curso
    dados_progresso["horas_curso"] = curso.quantidade_horas

    if progresso.nota != None:
      dados_progresso["nota"] = progresso.nota
    else:
      dados_progresso["nota"] = "Sem nota"

    if len(curso.lista_aulas) != 0:
      ptg_conc = (progresso.ultima_aula / len(curso.lista_aulas)) * 100
    else:
      ptg_conc = "0"
      
    dados_progresso["aula_concluida"] = ptg_conc

    return dados_progresso

  def todos_usuarios(self):
    lista_usuarios_email = []
    progressos = self.__dao.get_all()

    for progresso in progressos:
      if progresso.usuario_cod not in lista_usuarios_email:
        lista_usuarios_email.append(progresso.usuario_cod)

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
        self.__tela_progresso.close_opcao()
        self.__tela_progresso.close()
        self.relatorio_ind(values["email"][0])
        # self.informacao_user(usuario)
        return True

  def relatorio_ind(self, usuario_cod = None):
    if usuario_cod == None:
      usuario_cod = self.__controlador_sistema.usuario_logado.email

    self.__tela_progresso.close()
    lista_cursos = self.cursos_ja_cadastrado_por_usuario(usuario_cod)
    
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
          progresso = self.progresso_por_curso_e_usuario(curso.codigo, usuario_cod)
          self.__tela_progresso.close_opcao()
          self.detalhes_progresso(progresso)
          return True


  def gerar_certificado(self, progresso):
    if progresso.nota != None:
      dados = self.progresso_to_json(progresso)
      self.__controlador_sistema.controlador_certificado.criador(dados)
      self.__tela_progresso.show_message("Parab??ns", "Certificado salvo na pasta")

    else:
      self.__tela_progresso.show_message("Erro", "Curso n??o conclu??do")

  def detalhes_progresso(self, progresso):
    dados_progresso = self.progresso_to_json(progresso)
    button, values = self.__tela_progresso.open_opcao(2, dados_progresso)

    if button == 1:
      self.__tela_progresso.close_opcao()
      self.gerar_certificado(progresso)

    else:
      self.__tela_progresso.close_opcao()
        
  def cadastrar_no_curso(self, usuario = None):
    self.__tela_progresso.mostra_mensagem('Op????es de Cursos:')
    self.__controlador_sistema.controlador_curso.lista_cursos()
    self.__tela_progresso.mostra_mensagem("\nEntre com o nome do curso desejado...")
    entrada = self.__tela_progresso.pega_entrada("Nome: ")
    curso = self.__controlador_sistema.controlador_curso.pega_curso_por_nome(entrada)

    if curso != None:
      if self.progresso_por_curso_e_usuario(curso, usuario) != None:
        self.__tela_progresso.mostra_mensagem("Usu??rio j?? ?? cadastrado nesse curso")
      else:
        self.cria_progresso(curso, usuario)
        self.__tela_progresso.mostra_mensagem("Cadastrado no curso com sucesso")
        return True

    else:
      self.__tela_progresso.mostra_mensagem("Curso inexistente")
    
    return False

  def definir_ultima_aula(self, aula, curso, usuario = None):
    if type(curso) != int:
      curso = curso.codigo

    try:
      if usuario == None:
        usuario = self.__controlador_sistema.usuario_logado.email
      
      progresso = self.progresso_por_curso_e_usuario(curso, usuario)
      progresso.ultima_aula = aula
      return True
    except:
      return False

  def pegar_ultima_aula(self, curso, usuario_cod = None):
    try:
      if usuario_cod == None:
        usuario = self.__controlador_sistema.usuario_logado.email

      else:
        # caso receber um objeto ao inves da chave
        if type(usuario_cod) != str:
          usuario_cod = usuario_cod.email
      
      progresso = self.progresso_por_curso_e_usuario(curso, usuario_cod)
      return progresso.ultima_aula
    
    except:
      return None

  def dar_nota(self, progresso, nota):
    progresso.nota = nota
    self.__dao.update()

  def todos_progressos_por_usuario(self, usuario_cod):
    progressos_user = []
    progressos = self.__dao.get_all()

    for progresso in progressos:
      if progresso.usuario_cod == usuario_cod:
        progressos_user.append(progresso)

    return progressos_user
  
  def retornar(self):
    self.__tela_progresso.close()
    self.__tela_progresso.close_opcao()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    adm = self.__controlador_sistema.usuario_logado.adm
    lista_opcoes = {1: self.relatorio_ind, 2: self.todos_usuarios, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_progresso.open(adm)]()