from limite.telaUsuario import TelaUsuario
from entidade.usuario import Usuario
from dao.usuario_dao import usuarioDAO

class ControladorUsuario():
  def __init__(self, controlador_sistema):
    # self.__usuarios = []
    self.__tela_usuario = TelaUsuario()
    self.__controlador_sistema = controlador_sistema
    self.__dao = usuarioDAO()

  @property
  def usuarios(self):
    return self.__dao.get_all()

  def pega_usuario_por_email_e_senha(self, email: str, senha: str):
    try:
      usuario = self.__dao.get(email)
      if usuario.senha == senha:
        return usuario
    except:
      pass
    return None

  def pega_usuario_por_email(self, email: str):
    try:
      usuario = self.__dao.get(email)
      return usuario
    
    except:
      return None

  def criar_usuario(self, dados_usuario):
    usuario = Usuario(dados_usuario["nome"], dados_usuario["email"], dados_usuario["senha"], dados_usuario["adm"])
    self.cadastrar_usuario(usuario)
    return usuario

  def cadastrar_usuario(self, usuario):
    self.__dao.add(usuario)
  
  def cadastrar(self):
    while True:
      button, dados = self.__tela_usuario.open_opcao(3)

      if button == 0:
        self.__tela_usuario.close_opcao()

        # Essa verificacao serve pq pode ser para USUARIO ADM ou LOGIN
        if self.__tela_usuario.window != None:
          self.__tela_usuario.close()
        else:
          self.__controlador_sistema.controlador_login.tela_login.close()
        return False

      # Por padrão, novos usuarios não serão ADM. Um ADM deve setar outro ADM
      dados["adm"] = False

      if (dados["nome"] != '' and dados["nome"] != None) and (dados["email"] != '' and dados["email"] != None)\
          and (dados["senha"] != '' and dados["senha"] != None) and (dados["senha2"] != '' and dados["senha2"] != None):
        if dados["senha"] == dados["senha2"]:
          self.criar_usuario(dados)

          # Opcao para a tela no próprio usuário
          if self.__tela_usuario.window != None:
            self.__tela_usuario.show_message("Sucesso", "Usuário Cadastrado")
            self.__tela_usuario.close()

          # Opcao para tela no LOGIN            
          else:
            self.__tela_usuario.show_message("Bem Vindo", "Cadastrado com sucesso")
            self.__controlador_sistema.controlador_login.tela_login.close()
            
          self.__tela_usuario.close_opcao()
          return True

        self.__tela_usuario.show_message("Erro", "Senhas não correspondem")
      else:
        self.__tela_usuario.show_message("Erro", "Preencha todos os campos")

      self.__tela_usuario.close_opcao()

  def user_to_json(self, usuario):
    dados_usuario = {}
    dados_usuario["nome"] = usuario.nome
    dados_usuario["email"] = usuario.email
    dados_usuario["senha"] = usuario.senha
    dados_usuario["adm"] = usuario.adm

    return dados_usuario

  def alterar_usuario(self, usuario, novos_dados):
    try:
      usuario.nome = novos_dados["nome"]
      usuario.senha = novos_dados["senha"]
      usuario.adm = novos_dados["adm"]
      self.__dao.update()
      return True

    except:
      return False

  def alterar_usuario_info(self, usuario, adm = False):
    dados_antigos = self.user_to_json(usuario)
    button, values = self.__tela_usuario.open_edit_user(dados_antigos, adm)
    
    if adm == False:
      values["adm"] = False
    
    if button == 1:
      if self.alterar_usuario(usuario, values):
        self.__tela_usuario.show_message("Sucesso", "Dados alterados")
        self.__tela_usuario.close_opcao()
        self.__tela_usuario.close()

    elif button == 0:
      self.__tela_usuario.close_opcao()
      self.__tela_usuario.close()

  # card das informações do usuario, opcao de editar e excluir
  def informacao_user(self, usuario = None):
    self.__tela_usuario.close()

    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado

    dados_usuario = self.user_to_json(usuario)
    button, values = self.__tela_usuario.open_opcao(1, dados_usuario)
    
    if button == 0:
      self.__tela_usuario.close_opcao()

    elif button == 1:
      self.__tela_usuario.close_opcao()
      self.alterar_usuario_info(usuario, usuario.adm)

    elif button == 2:
      self.excluir_usuario(usuario)
      self.__tela_usuario.close_opcao()

  def lista_usuarios(self, usuario = None):
    lista_emails = []
    # for usuario in self.__usuarios:
    for usuario in self.__dao.get_all():
      lista_emails.append(usuario.email)

    while True:
      self.__tela_usuario.close()
      button, values = self.__tela_usuario.open_opcao(2, lista_emails)

      if button == 0:
        self.__tela_usuario.close_opcao()
        return False

      elif len(values["email"]) == 0:
        self.__tela_usuario.show_message("Erro", "Nenhum selecionado")
        self.__tela_usuario.close_opcao()
        return False

      else:
        usuario = self.pega_usuario_por_email(values["email"][0])
        self.__tela_usuario.close_opcao()
        self.informacao_user(usuario)
        return True

  def excluir_usuario(self, usuario = None):
    self.__tela_usuario.close()
    self.__tela_usuario.close_opcao()


    if (usuario != None):
      if self.__controlador_sistema.usuario_logado == usuario:
        self.__controlador_sistema.deslogar_usuario()

      self.__controlador_sistema.controlador_progresso.remove_progresso_por_usuario_cod(usuario.email)
      self.__dao.remove(usuario.email)
      self.__tela_usuario.show_message("Feito", "Usuario removido")

  def retornar(self):
    self.__tela_usuario.close()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    
    lista_opcoes_adm = {1: self.informacao_user, 2: self.lista_usuarios, 3: self.cadastrar, 0: self.retornar}
    continua = True
    while continua:
      adm = self.__controlador_sistema.usuario_logado.adm
      lista_opcoes_adm[self.__tela_usuario.open(adm)]()