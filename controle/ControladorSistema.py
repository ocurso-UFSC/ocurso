from limite.TelaSistema import TelaSistema
from controle.ControladorCurso import ControladorCurso
from controle.ControladorQuestao import ControladorQuestao
from controle.ControladorUsuario import ControladorUsuario
from controle.ControladorLogin import ControladorLogin

class ControladorSistema:
    def __init__(self, usuario_logado = None):
        self.__usuario_logado = usuario_logado
        self.__tela_sistema = TelaSistema()
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_questao = ControladorQuestao(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_login = ControladorLogin(self, self.__controlador_usuario)

   
    @property
    def controlador_questao(self):
        return self.__controlador_questao

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

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
        self.__controlador_usuario.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()

    def ver_curso(self):
        self.__controlador_curso.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        self.__tela_sistema.mostra_mensagem("\n")
        lista_opcoes = {1: self.usuario,  2: self.inclui_questao, 3: self.ver_curso, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()