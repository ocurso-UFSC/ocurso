from limite.TelaLogin import TelaLogin

class ControladorLogin():
  def __init__(self, controladorSistema, controladorUsuario):
    self.__tela_login = TelaLogin()
    self.__usuario_logado = None
    self.__controlador_usuario = controladorUsuario
    self.__controlador_sistema = controladorSistema

  def inicializa_sistema(self):
    self.abre_tela()

  def logar(self):
    dados_login = self.__tela_login.pega_login()
    usuario = self.__controlador_usuario.pega_usuario_por_email_e_senha(dados_login["email"], dados_login["senha"])
    
    if usuario != None:
      self.__tela_login.mostra_mensagem("Bem vindo {}" .format(usuario.nome))
      self.__usuario_logado = usuario
      print()
      return True
    
    self.__tela_login.mostra_mensagem("Usuário incorreto")
    return False

  def cadastrar(self):
    dados = self.__tela_login.pega_dados_cadastro()
    if dados["senha"] == dados["senha2"]:
      usuario = self.__controlador_usuario.criar_usuario(dados)
      self.__controlador_usuario.cadastrar_usuario(usuario)
      return True
    self.__tela_login.mostra_mensagem("Senhas não correspondem")
    return False

  def finaliza_sistema(self):
    self.__tela_login.mostra_mensagem("Até a próxima")
    exit()

  # funcao teste - logar automatico 
  def logar_automatico(self):
    dados = {"nome": "teste", "email": "teste", "senha": "123"}
    usuario = self.__controlador_usuario.criar_usuario(dados)
    self.__controlador_usuario.cadastrar_usuario(usuario)
    self.__usuario_logado = usuario
    print()

  def abre_tela(self):
    lista_opcoes = {1: self.logar, 2: self.cadastrar, 3: self.logar_automatico, 0: self.finaliza_sistema}
    
    while self.__usuario_logado == None:
      opcao_escolhida = self.__tela_login.tela_opcoes()
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()

    if self.__usuario_logado != None:
      self.__controlador_sistema.abre_tela()