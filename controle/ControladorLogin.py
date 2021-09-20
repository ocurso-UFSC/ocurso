from limite.TelaLogin import TelaLogin

class ControladorLogin:
  def __init__(self, controladorSistema):
    self.__tela_login = TelaLogin()
    self.__controlador_sistema = controladorSistema


  @property
  def tela_login(self):
    return self.__tela_login

  def inicializa_sistema(self):
    self.abre_tela()

  def logar(self):
    self.__tela_login.close()
    while True:
      dados_login = self.__tela_login.open_login()
      self.__tela_login.close_login()
      
      if (dados_login["email"] == "" or dados_login["email"] == None) and (dados_login["senha"] == "" or dados_login["senha"] == None):
        return False
      usuario = self.__controlador_sistema.controlador_usuario.pega_usuario_por_email_e_senha(dados_login["email"], dados_login["senha"])
      
      if usuario != None:
        self.__tela_login.show_message("Sucesso", "Bem vindo {}" .format(usuario.nome))
        self.__controlador_sistema.usuario_logado = usuario
        return True
      
      self.__tela_login.show_message("Erro", "Usuário ou Senhas inválidas")

  def cadastrar(self):
    self.__tela_login.close()
    self.__controlador_sistema.controlador_usuario.cadastrar()

  def finaliza_sistema(self):
    self.__tela_login.close()
    self.__tela_login.show_message("Bye", "Até a próxima")
    exit()

  def abre_tela(self):
    lista_opcoes = {1: self.logar, 2: self.cadastrar, 0: self.finaliza_sistema}
    
    while self.__controlador_sistema.usuario_logado == None:
      opcao_escolhida = self.__tela_login.open()
      
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()

    if self.__controlador_sistema != None:
      self.__controlador_sistema.abre_tela()