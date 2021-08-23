from entidade.questao import Questao
from limite.TelaQuestao import TelaQuestao

class ControladorQuestao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_questao = TelaQuestao()
        self.__questao = Questao
        self.__lista_questoes = []

    def incluir_questao(self):
        infos_questao = self.__tela_questao.infos_questao()
        questao = self.__questao(infos_questao['descricao_questao'], infos_questao['lista_alternativas'], infos_questao['alternativa_correta'])
        self.__lista_questoes.append(questao)

    def mostra_perguntas(self):
        print(self.__lista_questoes)

    def alterar_questao(self):
        numero = self.__tela_questao.alterando_questao()
        infos_questao = self.__tela_questao.infos_questao()
        self.__lista_questoes[numero - 1] = infos_questao
    
    def remover_questao(self):
        numero = self.__tela_questao.alterando_questao()
        self.__lista_questoes.pop(numero-1)

    def mostrar_respostas(self):
        self.__tela_questao.mostra_mensagem('\n---------- RESPOSTAS DA AVALIAÇÃO ----------\n')
        for q in range(len(self.__lista_questoes)):
            self.__tela_questao.mostra_resposta(q, self.__lista_questoes[q]['alternativa_correta'])
        self.__tela_questao.mostra_mensagem()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1:self.mostra_perguntas, 2: self.incluir_questao, 3:self.alterar_questao, 4:self.remover_questao, 9:self.mostrar_respostas, 0:self.retornar}

        continua = True
        while continua:
          lista_opcoes[self.__tela_questao.tela_opcoes()]()
