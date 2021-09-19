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

    def procura_questao_por_descricao(self, descricao=str):
        curso = self.__controlador_sistema.controlador_curso._ControladorCurso__curso_escolhido
        for questao in curso._Curso__avaliacao:
            if (questao._Questao__descricao_questao == descricao):
                return questao
            return None
    
    def cadastra_questao_aut(self, infos_questao, desc_alternativas):
        #infos_questao = {'descricao_questao':'descricao_questao', 'alternativa_correta': 'alternativa_correta'}
        #desc_alternativas = ["descricao_alternativa"]
        a1 = Alternativa("a", desc_alternativas[0])
        a2 = Alternativa("b", desc_alternativas[1])
        lista_alternativas = [a1, a2]

        questao = self.__questao(
                    infos_questao['descricao_questao'], 
                    lista_alternativas, 
                    infos_questao['alternativa_correta'])
        self.__controlador_sistema.controlador_curso.incluir_questao(questao)

    def incluir_questao(self):
        self.__tela_questao.close_window()
        infos_questao = self.__tela_questao.open_infos_questao()
        lista_alternativas = []
        alternativas_para_selecao = []
        quantidade_alternativas = infos_questao['quantidade_alternativas']
        for c in range (quantidade_alternativas):
            index = self.__indexes[c]
            descricao_alternativa = self.__tela_questao.open_alternativa(index)
            self.__tela_questao.close_window2()
            self.__alternativa = Alternativa(index, descricao_alternativa)
            lista_alternativas.append(self.__alternativa)
            alternativas_para_selecao.append(f'{index}) {descricao_alternativa}')

        alternativa_correta = self.__tela_questao.open_alternativa_correta(alternativas_para_selecao)
        self.__tela_questao.close_window2()

        questao = self.__questao(
                    infos_questao['descricao_questao'], 
                    lista_alternativas, 
                    alternativa_correta)
        self.__controlador_sistema.controlador_curso.incluir_questao(questao)
        self.__tela_questao.close_window3()

    def alterar_questao(self, numero):
        self.__tela_questao.close_window()
        infos_questao = self.__tela_questao.open_infos_questao()
        lista_alternativas = []
        alternativas_para_selecao = []
        quantidade_alternativas = infos_questao['quantidade_alternativas']
        for c in range (quantidade_alternativas):
            index = self.__indexes[c]
            descricao_alternativa = self.__tela_questao.open_alternativa(index)
            self.__tela_questao.close_window2()
            self.__alternativa = Alternativa(index, descricao_alternativa)
            lista_alternativas.append(self.__alternativa)
            alternativas_para_selecao.append(f'{index}) {descricao_alternativa}')

        alternativa_correta = self.__tela_questao.open_alternativa_correta(alternativas_para_selecao)
        self.__tela_questao.close_window2()

        questao = self.__questao(
                    infos_questao['descricao_questao'], 
                    lista_alternativas, 
                    alternativa_correta)
        self.__controlador_sistema.controlador_curso.alterar_questao(numero, questao)
        self.__tela_questao.close_window3()

    def mostra_perguntas(self):
        self.__tela_questao.close_window()
        curso = self.__controlador_sistema.controlador_curso._ControladorCurso__curso_escolhido
        nome_curso = curso._Curso__nome_do_curso
        self.__respostas_usuario[nome_curso] = list()
        cursos = self.__controlador_sistema.controlador_curso._ControladorCurso__cursos
        index_do_curso = cursos.index(self.__controlador_sistema.controlador_curso.pega_curso_por_nome(nome_curso))
        curso = cursos[index_do_curso]
        progresso = self.__controlador_sistema.controlador_progresso.progresso_por_curso_e_usuario(curso)
        if progresso._Progresso__ultima_aula == len(curso._Curso__lista_aulas):
            for questao in curso._Curso__avaliacao:
                alternativas = []
                for alternativa in questao._Questao__lista_alternativas:
                    alternativas.append(f'{alternativa._Alternativa__index} - {alternativa._Alternativa__descricao_alternativa}')
                resposta_usuario = self.__tela_questao.open_mostra_pergunta(f'{curso._Curso__avaliacao.index(questao)+1}) {questao._Questao__descricao_questao}', alternativas)
                self.__respostas_usuario[nome_curso].append(resposta_usuario)
                self.__tela_questao.close_window2()
        else:
            self.__tela_questao.show_message('Erro', 'Você precisa concluir todas as aulas \ndo curso para fazer a avaliação!')
    
    def remover_questao(self, numero):
        self.__controlador_sistema.controlador_curso.remover_questao(numero)

    def mostrar_respostas(self):
        self.__tela_questao.close_window()
        curso = self.__controlador_sistema.controlador_curso._ControladorCurso__curso_escolhido
        nome_curso = curso._Curso__nome_do_curso
        cursos = self.__controlador_sistema.controlador_curso._ControladorCurso__cursos
        index_do_curso = cursos.index(self.__controlador_sistema.controlador_curso.pega_curso_por_nome(nome_curso))
        curso = cursos[index_do_curso]
        acertos = 0
        # if len(self.__respostas_usuario[nome_curso] == 0:
        #     #Você ainda não realizou a avaliação deste curso!

        if nome_curso not in self.__respostas_usuario:
            self.__tela_questao.show_message(f'Atenção!', 'Você ainda não realizou a avaliação deste curso.')

        else:
            for resposta in range (len(self.__respostas_usuario[nome_curso])):
                if self.__respostas_usuario[nome_curso][resposta] == curso._Curso__avaliacao[resposta]._Questao__alternativa_correta:
                    acertos += 1

            progresso = self.__controlador_sistema.controlador_progresso.progresso_por_curso_e_usuario(curso)
            progresso.nota = acertos/len(self.__respostas_usuario[nome_curso]) * 10
            # self.__nota_usuario[nome_curso] = acertos/len(self.__respostas_usuario[nome_curso]) * 10
            self.__tela_questao.open_mostra_mensagem(f'Sua nota em {nome_curso.upper()} é', progresso.nota)
        self.__tela_questao.close_window2()
    
    def listar_questoes(self):
        curso = self.__controlador_sistema.controlador_curso._ControladorCurso__curso_escolhido
        lista_de_questoes = []
        for questao in curso._Curso__avaliacao:
            lista_de_questoes.append(questao._Questao__descricao_questao)
        while True:
            button, values = self.__tela_questao.open_listar_questoes(lista_de_questoes)

            if button == 0:
                self.__tela_questao.close_window2()
                return False
            elif len(values["questao"]) == 0:
                self.__tela_questao.show_message("Erro", "Nenhuma questão selecionada")
                self.__tela_questao.close_window2()
                return False
            elif button == 1:
                self.__tela_questao.close_window2()
                questao = self.procura_questao_por_descricao(values['questao'][0])
                curso = self.__controlador_sistema.controlador_curso._ControladorCurso__curso_escolhido
                numero_questao = curso._Curso__avaliacao.index(questao)
                self.alterar_questao(numero_questao)
                return False

            elif button == 2:
                self.__tela_questao.close_window2()
                questao = self.procura_questao_por_descricao(values['questao'][0])
                curso = self.__controlador_sistema.controlador_curso._ControladorCurso__curso_escolhido
                numero_questao = curso._Curso__avaliacao.index(questao)
                self.remover_questao(numero_questao)
                return False

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1:self.mostra_perguntas, 2: self.incluir_questao, 5:self.listar_questoes, 9:self.mostrar_respostas, 0:self.retornar}

        continua = True
        while continua:
          lista_opcoes[self.__tela_questao.open_window()]()
