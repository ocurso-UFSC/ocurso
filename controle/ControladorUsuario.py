from limite.telaUsuario import TelaUsuario
from entidade.usuario import Usuario

class ControladorUsuario():
  def __init__(self, controlador_sistema):
    self.__usuarios = []
    self.__tela_usuario = TelaUsuario()
    self.__controlador_sistema = controlador_sistema

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

  def cadastrar_usuario(self, usuario):
    self.__usuarios.append(usuario)

  def incluir_usuario(self):
    dados_usuario = self.__tela_usuario.pega_dados_usuario()
    usuario = Usuario(dados_usuario["nome"], dados_usuario["email"], dados_usuario["senha"])
    self.__usuarios.append(usuario)

  def alterar_usuario(self, usuario = None):
    # Em caso de ser ADM
    if usuario == None:
      self.lista_usuarios()
      email_usuario = self.__tela_usuario.seleciona_usuario()
      usuario = self.pega_usuario_por_email(email_usuario)

    # Em caso de nao ser ADM
    else: 
      self.__tela_usuario.mostra_mensagem("Alterando seus dados")

    # Solicitacao de novos dados
    if (usuario != None):
      novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
      usuario.nome = novos_dados_usuario["nome"]
      usuario.email = novos_dados_usuario["email"]
      usuario.senha = novos_dados_usuario["senha"]
      self.lista_usuarios()

    # Caso o 'pega_usuario_por_email' retornar 'Null'
    else:
      self.__tela_usuario.mostra_mensagem("ATENÇÃO!!! Usuário inexistente")

  def lista_usuarios(self, usuario = None):
    if len(self.__usuarios) == 0:
      self.__tela_usuario.mostra_mensagem("nenhum usuario cadastrado")

    # Em caso de usuario comum
    if usuario != None:
      self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "email": usuario.email, "senha": usuario.senha, "adm": usuario.adm})

    # Em caso de ADM
    else:
      for usuario in self.__usuarios:
        self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "email": usuario.email, "senha": usuario.senha, "adm": usuario.adm})

  def mostra_usuario_logado(self):
    self.lista_usuarios(self.__controlador_sistema.usuario_logado)

  def excluir_usuario(self):
    self.lista_usuarios()
    email_usuario = self.__tela_usuario.seleciona_usuario()
    usuario = self.pega_usuario_por_email(email_usuario)

    if (usuario != None):
      self.__usuarios.remove(usuario)
      self.lista_usuarios()
    else:
      self.__tela_usuario.mostra_mensagem("ATENÇÃO!!! Usuário inexistente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.mostra_usuario_logado, 2: self.incluir_usuario, 3: self.alterar_usuario, 4: self.lista_usuarios, 5: self.excluir_usuario, 0: self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_usuario.tela_opcoes()]()
