#from entidade.questao import Questao
from limite.TelaQuestao import TelaQuestao

class ControladorQuestao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
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
        self.__tela_questao = TelaQuestao()
    
    def incluir_questao(self):
        infos_questao = self.__tela_questao.infos_questao()
        self.__questoes.append(infos_questao)
    
    def mostra_perguntas(self):
        for q in range(len(self.__questoes)):
            self.__tela_questao.mostra_descricao(self.__questoes[q]['descricao_questao'])
            for resposta_alternativa, index_questao in self.__questoes[q]['alternativas'].items():
                index = index_questao
                resposta = resposta_alternativa

                self.__tela_questao.mostra_pergunta(index, resposta)
            
        # self.__tela_questao.mostra_pergunta(alternativas=self.__questoes[1]['alternativas'])
        # self.__tela_questao.mostra_pergunta(alternativa_correta=self.__questoes[1]['alternativa_correta'])


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {2: self.incluir_questao, 1:self.mostra_perguntas, 0:self.retornar}

        continua = True
        while continua:
          lista_opcoes[self.__tela_questao.tela_opcoes()]()
