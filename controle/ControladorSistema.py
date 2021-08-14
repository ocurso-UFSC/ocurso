from limite.TelaSistema import TelaSistema
# from controle.ControladorAvaliacao import ControladorAvaliacao
from controle.ControladorAula import ControladorAula
from controle.ControladorCurso import ControladorCurso
from controle.ControladorQuestao import ControladorQuestao
from controle.ControladorUsuario import ControladorUsuarios

class ControladorSistema:
    def __init__(self):
        # self.__controlador_avaliacao = ControladorQuestao(self)
        # self.__controlador_aula = ControladorAula(self)
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_questao = ControladorQuestao(self)
        # self.__controlador_usuarios = ControladorUsuarios(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_questao(self):
        return self.__controlador_questao

    def inicializa_sistema(self):
        self.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()

    def ver_curso(self):
        self.__controlador_curso.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_questao, 0: self.encerra_sistema, 4: self.ver_curso}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()