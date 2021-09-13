from entidade.alternativa import Alternativa
from entidade.questao import Questao
from limite.TelaQuestao import TelaQuestao

class ControladorQuestao():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_questao = TelaQuestao()
        self.__questao = Questao
        self.__respostas_usuario = {}
        self.__indexes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        # self.__nota_usuario = {} # levar para a classe Usuario | "nome curso, nota usuario"

    
    def cadastra_questao_aut(self, nome_curso, infos_questao, desc_alternativas):
        #infos_questao = {'descricao_questao':'descricao_questao', 'alternativa_correta': 'alternativa_correta'}
        #lista_alternativas = ["descricao_alternativa"]
        a1 = Alternativa("a", desc_alternativas[0])
        a2 = Alternativa("b", desc_alternativas[1])
        lista_alternativas = [a1, a2]

        questao = self.__questao(
                    infos_questao['descricao_questao'], 
                    lista_alternativas, 
                    infos_questao['alternativa_correta'])
        self.__controlador_sistema.controlador_curso.incluir_questao(nome_curso, questao)

    def incluir_questao(self):
        nome_curso = self.__tela_questao.nome_curso()
        infos_questao = self.__tela_questao.infos_questao()
        lista_alternativas = []
        quantidade_alternativas = self.__tela_questao.quantidade('Quantas alternativas você deseja ter na questão? ')
        for c in range (quantidade_alternativas):
            index = self.__indexes[c]
            descricao_alternativa = self.__tela_questao.alternativa(f'Digite a descrição da alternativa {index}: ')
            self.__alternativa = Alternativa(index, descricao_alternativa)
            lista_alternativas.append(self.__alternativa)

        questao = self.__questao(
                    infos_questao['descricao_questao'], 
                    lista_alternativas, 
                    infos_questao['alternativa_correta'])
        self.__controlador_sistema.controlador_curso.incluir_questao(nome_curso, questao)

    def mostra_perguntas(self):
        nome_curso = self.__tela_questao.nome_curso()
        self.__respostas_usuario[nome_curso] = list()
        cursos = self.__controlador_sistema.controlador_curso._ControladorCurso__cursos
        index_do_curso = cursos.index(self.__controlador_sistema.controlador_curso.pega_curso_por_nome(nome_curso))
        curso = cursos[index_do_curso]
        for questao in curso._Curso__avaliacao:
            self.__tela_questao.mostra_descricao(curso._Curso__avaliacao.index(questao) + 1, questao._Questao__descricao_questao)       #self.__lista_questoes.index(q) + 1
            for alternativa in questao._Questao__lista_alternativas:
                self.__tela_questao.mostra_pergunta(alternativa._Alternativa__index, alternativa._Alternativa__descricao_alternativa)
            
            resposta_usuario = self.__tela_questao.pega_resposta()
            self.__respostas_usuario[nome_curso].append(resposta_usuario)

    def alterar_questao(self):
        nome_curso = self.__tela_questao.nome_curso()
        numero = self.__tela_questao.alterando_questao()
        infos_questao = self.__tela_questao.infos_questao()
        lista_alternativas = []
        quantidade_alternativas = self.__tela_questao.quantidade('Quantas alternativas você deseja ter na questão? ')
        for c in range (quantidade_alternativas):
            index = self.__indexes[c]
            descricao_alternativa = self.__tela_questao.alternativa(f'Digite a descrição da alternativa {index}: ')
            self.__alternativa = Alternativa(index, descricao_alternativa)
            lista_alternativas.append(self.__alternativa)

        questao = self.__questao(
                    infos_questao['descricao_questao'], 
                    lista_alternativas, 
                    infos_questao['alternativa_correta'])
        self.__controlador_sistema.controlador_curso.alterar_questao(nome_curso, numero, questao)
    
    def remover_questao(self):
        nome_curso = self.__tela_questao.nome_curso()
        numero_questao = self.__tela_questao.alterando_questao()
        self.__controlador_sistema.controlador_curso.remover_questao(nome_curso, numero_questao)

    def mostrar_respostas(self):
        nome_curso = self.__tela_questao.nome_curso()
        cursos = self.__controlador_sistema.controlador_curso._ControladorCurso__cursos
        index_do_curso = cursos.index(self.__controlador_sistema.controlador_curso.pega_curso_por_nome(nome_curso))
        curso = cursos[index_do_curso]
        self.__tela_questao.mostra_mensagem('\n---------- NOTA FINAL DA AVALIAÇÃO ----------\n')
        acertos = 0
        for resposta in range (len(self.__respostas_usuario[nome_curso])):
            if self.__respostas_usuario[nome_curso][resposta] == curso._Curso__avaliacao[resposta]._Questao__alternativa_correta:
                acertos += 1

        progresso = self.__controlador_sistema.controlador_progresso.progresso_por_curso_e_usuario(curso)
        progresso.nota = acertos/len(self.__respostas_usuario[nome_curso]) * 10
        # self.__nota_usuario[nome_curso] = acertos/len(self.__respostas_usuario[nome_curso]) * 10
        self.__tela_questao.mostra_mensagem(f'Sua nota na avaliação de {nome_curso.upper()} é {progresso.nota}\n')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1:self.mostra_perguntas, 2: self.incluir_questao, 3:self.alterar_questao, 4:self.remover_questao, 9:self.mostrar_respostas, 0:self.retornar}

        continua = True
        while continua:
          lista_opcoes[self.__tela_questao.tela_opcoes()]()
