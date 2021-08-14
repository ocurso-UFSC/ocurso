from limite.telaUsuario import TelaUsuario
from entidade.usuario import Usuario

class ControladorUsuarios():
  def __init__(self, controlador_sistema):
    self.__usuarios = []
    self.__tela_usuario = TelaUsuario()
    self.__controlador_sistema = controlador_sistema

  def pega_usuario_por_email(self, email: str):
    for usuario in self.__usuarios:
      if (usuario.email == email):
        return usuario
    return None

  def incluir_usuario(self):
    dados_usuario = self.__tela_usuario.pega_dados_usuario()
    usuario = Usuario(dados_usuario["nome"], dados_usuario["email"], dados_usuario["senha"])
    self.__usuarios.append(usuario)

  def alterar_usuario(self):
    self.lista_usuarios()
    email_usuario = self.__tela_usuario.seleciona_usuario()
    usuario = self.pega_usuario_por_email(email_usuario)

    if (usuario != None):
      novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
      usuario.nome = novos_dados_usuario["nome"]
      usuario.email = novos_dados_usuario["email"]
      usuario.senha = novos_dados_usuario["senha"]
      self.lista_usuarios()

    else:
      self.__tela_usuario.mostra_mensagem("ATENÇÃO!!! Usuário inexistente")

  def logar(self):
    dados_login = self.__tela_usuario.pega_login()
    for usuario in self.__usuarios:
      if ((dados_login["email"] == usuario.email) and (dados_login["senha"] == usuario.senha)):
        return usuario
    return None

  def lista_usuarios(self):
    if len(self.__usuarios) == 0:
      print("Lista de usuários está vazia")

    for usuario in self.__usuarios:
      self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "email": usuario.telefone, "senha": usuario.cpf})

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
    lista_opcoes = {1: self.logar, 2: self.incluir_usuario, 3: self.alterar_usuario, 4: self.lista_usuarios, 5: self.excluir_usuario, 0: self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_usuario.tela_opcoes()]()