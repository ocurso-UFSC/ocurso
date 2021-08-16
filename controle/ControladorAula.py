from limite.TelaAula import TelaAula
from entidade.curso import Curso
# from entidade.aula import Aula

class ControladorAula():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aula = TelaAula()
        self.__conteudos = [
                        {'descricao':'O Python é uma linguagem de programação',
                        'link':'https://link.python.conteudo'},
                        {'descricao':'É uma linguagem orientada ao objeto',
                        'link':'https://link.python.orientadoaobjeto'},
        ]
    
    def acessar_conteudo(self):
        for c in range (len(self.__conteudos)):
            self.__tela_aula.mostra_aulas(self.__conteudos[c]['descricao'], self.__conteudos[c]['link'])

    def adicionar_conteudo(self):
        ...

    def editar_conteudo(self):
        ...

    def remover_conteudo(self):
        ...

    def retornar_curso(self):
        self.__controlador_sistema.ver_curso()

    def abre_tela(self):
        lista_opcoes = {1: self.acessar_conteudo, 2:self.adicionar_conteudo, 3:self.editar_conteudo, 4:self.remover_conteudo, 0:self.retornar_curso}

        while True:
            lista_opcoes[self.__tela_aula.tela_opcoes()]()
