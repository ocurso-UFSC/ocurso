from limite.TelaLogin import TelaLogin

class ControladorLogin:
  __instance = None

  def __init__(self, controladorSistema):
    self.__tela_login = TelaLogin()
    self.__controlador_sistema = controladorSistema

  def inicializa_sistema(self):
    # self.abre_tela()
    (botao, dados) = self.__tela_login.open()

  def logar(self):
    while True:
      dados_login = self.__tela_login.open_login()
      usuario = self.__controlador_sistema.controlador_usuario.pega_usuario_por_email_e_senha(dados_login["email"], dados_login["senha"])
      
      if usuario != None:
        self.__tela_login.show_message("Sucesso", "Bem vindo {}" .format(usuario.nome))
        self.__controlador_sistema.usuario_logado = usuario
        self.__tela_login.close_login()
        self.__tela_login.close()
        return True
      
      self.__tela_login.show_message("Erro", "Usuário ou Senhas inválidas")
      self.__tela_login.close_login()

  def cadastrar(self):
    while True:
      dados = self.__tela_login.open_cadastro()
      dados["adm"] = "s"
      if (dados["nome"] != '' and dados["nome"] != None) and (dados["email"] != '' and dados["email"] != None)\
          and (dados["senha"] != '' and dados["senha"] != None) and (dados["senha2"] != '' and dados["senha2"] != None):
        if dados["senha"] == dados["senha2"]:
          if dados["adm"].lower() == "s" or dados["adm"].lower() == "sim":
            dados["adm"] = True
          elif dados["adm"].lower() == "n" or dados["adm"].lower() == "nao":
            dados["adm"] = False
          else:
            self.__tela_login.mostra_mensagem("Opcao ADM inválida")
            self.__tela_login.close_cadastro()
            return False
          usuario = self.__controlador_sistema.controlador_usuario.criar_usuario(dados)
          self.__controlador_sistema.controlador_usuario.cadastrar_usuario(usuario)
          self.__tela_login.show_message("Bem Vindo", "Cadastrado com sucesso")
          self.__tela_login.close_cadastro()
          return True

        self.__tela_login.show_message("Erro", "Senhas não correspondem")
      else:
        self.__tela_login.show_message("Erro", "Preencha todas as caixas")

      self.__tela_login.close_cadastro()

  def finaliza_sistema(self):
    self.__tela_login.mostra_mensagem("Até a próxima")
    exit()

  # funcao teste - logar automatico 
  def logar_visitante(self):
    dados = {"nome": "visitante", "email": "visitante", "senha": "visitante", "adm": True}
    usuario = self.__controlador_sistema.controlador_usuario.criar_usuario(dados)
    self.__controlador_sistema.controlador_usuario.cadastrar_usuario(usuario)
    self.__controlador_sistema.usuario_logado = usuario
    self.__tela_login.close()

  def abre_tela(self):
    lista_opcoes = {1: self.logar, 2: self.cadastrar, 3: self.logar_visitante, 0: self.finaliza_sistema}
    
    while self.__controlador_sistema.usuario_logado == None:
      opcao_escolhida = self.__tela_login.open()
      
      funcao_escolhida = lista_opcoes[opcao_escolhida]
      funcao_escolhida()

    if self.__controlador_sistema != None:
      self.__controlador_sistema.abre_tela()