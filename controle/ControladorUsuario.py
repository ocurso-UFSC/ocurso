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


  def alterar_meus_dados(self):
    self.__tela_usuario.mostra_mensagem("Alterando seus dados")
    self.__tela_usuario.mostra_mensagem("\n")
    self.minha_informacao()
    self.__tela_usuario.mostra_mensagem("Entre com os novos dados: ")
    novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
    self.__controlador_sistema.usuario_logado.nome = novos_dados_usuario["nome"]
    self.__controlador_sistema.usuario_logado.email = novos_dados_usuario["email"]
    self.__controlador_sistema.usuario_logado.senha = novos_dados_usuario["senha"]

    self.__tela_usuario.mostra_mensagem("\n")

  def alterar_usuario(self):
    # Em caso de ser ADM
    if self.__controlador_sistema.usuario_logado.adm == True:
      self.lista_usuarios()
      email_usuario = self.__tela_usuario.seleciona_usuario()
      usuario = self.pega_usuario_por_email(email_usuario)

      # Solicitacao de novos dados
      if (usuario != None):
        novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
      
      if novos_dados_usuario["adm"].lower() == "s" or novos_dados_usuario["adm"].lower() == "sim":
        novos_dados_usuario["adm"] = True
      elif novos_dados_usuario["adm"].lower() == "n" or novos_dados_usuario["adm"].lower() == "nao":
        novos_dados_usuario["adm"] = False
      else:
        self.__tela_login.mostra_mensagem("Opcao ADM inválida")
        return False

      usuario.nome = novos_dados_usuario["nome"]
      usuario.email = novos_dados_usuario["email"]
      usuario.senha = novos_dados_usuario["senha"]
      usuario.adm = novos_dados_usuario["adm"]
      self.__tela_usuario.mostra_mensagem("\n")

    # Caso o 'pega_usuario_por_email' retornar 'Null'
    else:
      self.__tela_usuario.mostra_mensagem("ATENÇÃO!!! Usuário inexistente")

  def minha_informacao(self):
    usuario = self.__controlador_sistema.usuario_logado
    self.__tela_usuario.mostra_mensagem("Minhas informações")
    self.__tela_usuario.mostra_usuario(usuario)

  def lista_usuarios(self, usuario = None):
    if len(self.__usuarios) == 0:
      self.__tela_usuario.mostra_mensagem("Nenhum usuário cadastrado")

    for usuario in self.__usuarios:
      self.__tela_usuario.mostra_mensagem("Todos os usuários cadastrados")
      self.__tela_usuario.mostra_usuario(usuario)


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
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.minha_informacao, 2: self.alterar_meus_dados, 3: self.excluir_minha_conta, 0: self.retornar}
    lista_opcoes_adm = {1: self.minha_informacao, 2: self.lista_usuarios, 3: self.alterar_meus_dados, 4: self.incluir_usuario, 
                          5: self.alterar_usuario, 6: self.excluir_usuario, 7: self.excluir_minha_conta, 0: self.retornar}
    continua = True
    while continua:

      if self.__controlador_sistema.usuario_logado.adm == True:
        lista_opcoes_adm[self.__tela_usuario.tela_opcoes_adm()]()
      else:
        lista_opcoes[self.__tela_usuario.tela_opcoes()]()