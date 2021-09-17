from limite.telaUsuario import TelaUsuario
from entidade.usuario import Usuario

class ControladorUsuario():
  def __init__(self, controlador_sistema):
    self.__usuarios = []
    self.__tela_usuario = TelaUsuario()
    self.__controlador_sistema = controlador_sistema

  @property
  def usuarios(self):
    return self.__usuarios

  def pega_usuario_por_email_e_senha(self, email: str, senha: str):
    for usuario in self.__usuarios:
      if (usuario.email == email) and (usuario.senha == senha):
        return usuario
      return None

  def pega_usuario_por_email(self, email: str):
    for usuario in self.__usuarios:
      if (usuario.email == email):
        return usuario
    return None

  def criar_usuario(self, dados_usuario):
    usuario = Usuario(dados_usuario["nome"], dados_usuario["email"], dados_usuario["senha"], dados_usuario["adm"])
    self.cadastrar_usuario(usuario)
    return usuario

  def cadastrar_usuario(self, usuario):
    self.__usuarios.append(usuario)

  
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

      dados["adm"] = "s"

      if (dados["nome"] != '' and dados["nome"] != None) and (dados["email"] != '' and dados["email"] != None)\
          and (dados["senha"] != '' and dados["senha"] != None) and (dados["senha2"] != '' and dados["senha2"] != None):
        if dados["senha"] == dados["senha2"]:
          if dados["adm"].lower() == "s" or dados["adm"].lower() == "sim":
            dados["adm"] = True
          elif dados["adm"].lower() == "n" or dados["adm"].lower() == "nao":
            dados["adm"] = False
          else:
            self.__tela_usuario.mostra_mensagem("Opcao ADM inválida")
            self.__tela_usuario.close_opcao()
            return False
          self.criar_usuario(dados)

          if self.__tela_usuario.window != None:
            self.__tela_usuario.show_message("Sucesso", "Usuário Cadastrado")
            self.__tela_usuario.close()
            
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
      usuario.email = novos_dados["email"]
      usuario.senha = novos_dados["senha"]
      usuario.adm = novos_dados["adm"]
      
      return True

    except:
      return False

  def alterar_usuario_info(self, usuario):
    dados_antigos = self.user_to_json(usuario)
    button, values = self.__tela_usuario.open_edit_user(dados_antigos)
    
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
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado
    
    dados_usuario = self.user_to_json(usuario)
    button, values = self.__tela_usuario.open_opcao(1, dados_usuario)
    
    if button == 0:
      self.__tela_usuario.close_opcao()
      self.__tela_usuario.close()

    elif button == 1:
      self.__tela_usuario.close_opcao()
      self.__tela_usuario.close()
      self.alterar_usuario_info(usuario)

    elif button == 2:
      self.excluir_usuario(usuario)
      self.__tela_usuario.close_opcao()

  def lista_usuarios(self, usuario = None):
    if len(self.__usuarios) == 0:
      self.__tela_usuario.mostra_mensagem("Nenhum usuário cadastrado")

    lista_emails = []
    for usuario in self.__usuarios:
      lista_emails.append(usuario.email)

    while True:

      button, values = self.__tela_usuario.open_opcao(2, lista_emails)

      if button == 0:
        self.__tela_usuario.close_opcao()
        self.__tela_usuario.close()
        return False

      elif len(values["email"]) == 0:
        self.__tela_usuario.show_message("Erro", "Nenhum selecionado")
        self.__tela_usuario.close_opcao()
        self.__tela_usuario.close()
        return False

      else:
        usuario = self.pega_usuario_por_email(values["email"][0])
        self.__tela_usuario.close_opcao()
        self.__tela_usuario.close()
        self.informacao_user(usuario)
        return True

  def mostra_usuario_logado(self):
    self.lista_usuarios(self.__controlador_sistema.usuario_logado)

  def excluir_usuario(self, usuario = None):
    if (usuario != None):
      if self.__controlador_sistema.usuario_logado == usuario:
        self.__tela_usuario.close()
        self.__tela_usuario.close_opcao()
        self.__controlador_sistema.deslogar_usuario()

      self.__usuarios.remove(usuario)
      self.__tela_usuario.show_message("Feito", "Usuario removido")

  def retornar(self):
    self.__tela_usuario.close()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    
    lista_opcoes_adm = {1: self.informacao_user, 2: self.lista_usuarios, 3: self.cadastrar, 0: self.retornar}
    continua = True
    while continua:
      if self.__controlador_sistema.usuario_logado.adm == True:
        lista_opcoes_adm[self.__tela_usuario.open()]()

      else:
        pass