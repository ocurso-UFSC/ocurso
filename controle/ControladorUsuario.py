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

  def incluir_usuario(self):
    self.__tela_usuario.mostra_mensagem("\nEntre com os dados")
    dados = self.__tela_usuario.pega_dados_usuario()

    if dados["adm"].lower() == "s" or dados["adm"].lower() == "sim":
      dados["adm"] = True
    elif dados["adm"].lower() == "n" or dados["adm"].lower() == "nao":
      dados["adm"] = False
    
    else:
      self.__tela_login.mostra_mensagem("Opcao ADM inválida")
      return False

    usuario = Usuario(dados["nome"], dados["email"], dados["senha"], dados["adm"])
    self.__usuarios.append(usuario)
    return False


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

    elif button == 0:
      self.__tela_usuario.close_opcao()

  def informacao_user(self, usuario = None):
    if usuario == None:
      usuario = self.__controlador_sistema.usuario_logado
    
    dados_usuario = self.user_to_json(usuario)
    button, values = self.__tela_usuario.open_opcao(1, dados_usuario)
    
    if button == 0:
      self.__tela_usuario.close_opcao()

    elif button == 1:
      self.__tela_usuario.close_opcao()
      self.alterar_usuario_info(usuario)

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

  def mostra_usuario_logado(self):
    self.lista_usuarios(self.__controlador_sistema.usuario_logado)

  def excluir_minha_conta(self):
    self.__tela_usuario.mostra_mensagem("Adeus")
    self.excluir_usuario(self.__controlador_sistema.usuario_logado)
    exit()

  def excluir_usuario(self, usuario = None):
    if usuario == None:
      email_usuario = self.__tela_usuario.seleciona_usuario()
      usuario = self.pega_usuario_por_email(email_usuario)

    if (usuario != None):
      self.__usuarios.remove(usuario)
      self.__tela_usuario.mostra_mensagem("Usuario removido")

    else:
      self.__tela_usuario.mostra_mensagem("ATENÇÃO!!! Usuário inexistente")

  def retornar(self):
    self.__tela_usuario.close()
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    # lista_opcoes = {1: self.minha_informacao, 2: self.alterar_meus_dados, 3: self.excluir_minha_conta, 0: self.retornar}
    
    lista_opcoes_adm = {1: self.informacao_user, 2: self.lista_usuarios, 4: self.incluir_usuario, 0: self.retornar}
    continua = True
    while continua:

      # em caso de ADM
      if self.__controlador_sistema.usuario_logado.adm == True:
        lista_opcoes_adm[self.__tela_usuario.open()]()

      # em caso de NÃO ADM
      else:
        # lista_opcoes[self.__tela_usuario.tela_opcoes()]()
        pass