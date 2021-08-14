# from entidade.questao import Questao
from limite.TelaQuestao import TelaQuestao

class ControladorQuestao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__questoes = {}
        self.__tela_questao = TelaQuestao()
    
    def incluir_questao(self):
        infos_questao = self.__tela_questao.infos_questao()
        self.__questoes['Questão' + str(len(self.__questoes)+1)] = infos_questao

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_questao, 0:self.retornar}

        continua = True
        while continua:
          lista_opcoes[self.__tela_questao.tela_opcoes()]()
