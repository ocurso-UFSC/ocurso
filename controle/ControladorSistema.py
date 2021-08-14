from limite.TelaSistema import TelaSistema
from controle.ControladorQuestao import ControladorQuestao

class ControladorSistema:
    def __init__(self):
        self.__controlador_questao = ControladorQuestao(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_questao(self):
        return self.__controlador_questao

    def inicializa_sistema(self):
        self.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_questao, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()