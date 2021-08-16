#from entidade.questao import Questao
from limite.TelaQuestao import TelaQuestao

class ControladorQuestao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_questao = TelaQuestao()
        self.__questoes = [
                    {
                        'descricao_questao':'Quanto é 2+2?',
                        'alternativas':{'a':'2', 'b':'4', 'c':'8'},
                        'alternativa_correta':'b',
                    },
                    {
                        'descricao_questao':'Quem descobriu o Brasil?',
                        'alternativas':{'a':'Neymar', 'b':'Jean Hauck', 'c':'Pedro Alvares Cabral'},
                        'alternativa_correta':'c',
                    },
        ]

    def mostra_perguntas(self):
        self.__tela_questao.mostra_mensagem('\n---------- AVALIAÇÃO FINAL ----------\n')      #trocar para mostrar msg
        for q in range(len(self.__questoes)):
            self.__tela_questao.mostra_descricao(q+1, self.__questoes[q]['descricao_questao'])
            for resposta_alternativa, index_questao in self.__questoes[q]['alternativas'].items():
                index = index_questao
                resposta = resposta_alternativa

                self.__tela_questao.mostra_pergunta(index, resposta)
            self.__tela_questao.mostra_mensagem('')
        self.__tela_questao.mostra_mensagem('Responda as questões e guarde suas respostas para comparar com as corretas mais tarde.\n')
    
    def incluir_questao(self):
        infos_questao = self.__tela_questao.infos_questao()
        self.__questoes.append(infos_questao)
    
    def alterar_questao(self):
        numero = self.__tela_questao.alterando_questao()
        infos_questao = self.__tela_questao.infos_questao()
        self.__questoes[numero - 1] = infos_questao
    
    def remover_questao(self):
        numero = self.__tela_questao.alterando_questao()
        self.__questoes.pop(numero-1)

    def mostrar_respostas(self):
        self.__tela_questao.mostra_mensagem('\n---------- RESPOSTAS DA AVALIAÇÃO ----------\n')
        for q in range(len(self.__questoes)):
            self.__tela_questao.mostra_resposta(q, self.__questoes[q]['alternativa_correta'])
        self.__tela_questao.mostra_mensagem()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1:self.mostra_perguntas, 2: self.incluir_questao, 3:self.alterar_questao, 4:self.remover_questao, 9:self.mostrar_respostas, 0:self.retornar}

        continua = True
        while continua:
          lista_opcoes[self.__tela_questao.tela_opcoes()]()
