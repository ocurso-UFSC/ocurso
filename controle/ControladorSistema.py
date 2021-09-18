from limite.TelaSistema import TelaSistema
from controle.ControladorCurso import ControladorCurso
from controle.ControladorQuestao import ControladorQuestao
from controle.ControladorUsuario import ControladorUsuario
from controle.ControladorLogin import ControladorLogin
from controle.ControladorAula import ControladorAula
from controle.ControladorProgresso import ControladorProgresso

class ControladorSistema:
    __instance = None

    def __init__(self, usuario_logado = None):
        self.__tela_sistema = TelaSistema()
        self.__usuario_logado = usuario_logado
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_questao = ControladorQuestao(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_login = ControladorLogin(self)
        self.__controlador_aula = ControladorAula(self)
        self.__controlador_progresso = ControladorProgresso(self)
    
    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    @property
    def controlador_curso(self):
        return self.__controlador_curso

    @property
    def controlador_aula(self):
        return self.__controlador_aula

    @property
    def controlador_questao(self):
        return self.__controlador_questao

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

    @property
    def controlador_login(self):
        return self.__controlador_login

    @property
    def controlador_progresso(self):
        return self.__controlador_progresso

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, usuario_logado):
        self.__usuario_logado = usuario_logado

    def inicializa_sistema(self):
        if self.__usuario_logado == None:
            self.__controlador_login.abre_tela()
        else:
            self.abre_tela()

    def usuario(self):
        self.__tela_sistema.close()
        self.__controlador_usuario.abre_tela()

    def ver_curso(self):
        self.__tela_sistema.close()
        self.__controlador_curso.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()
    
    def abre_aulas(self):
        self.__controlador_aula.abre_tela()

    def deslogar_usuario(self):
        self.__tela_sistema.mostra_mensagem("Usuário Deslogado")
        self.__usuario_logado = None
        self.__tela_sistema.close()
        self.__controlador_login.inicializa_sistema()
          
    def progresso(self):
        self.__tela_sistema.close()
        self.__controlador_progresso.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.usuario, 2: self.ver_curso, 3: self.progresso, 0: self.deslogar_usuario}

        while True:
            opcao_escolhida = self.__tela_sistema.open()
            
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
        self.__tela_sistema.close()
