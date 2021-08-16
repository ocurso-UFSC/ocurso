from limite.TelaAula import TelaAula
# from entidade.aula import Aula

class ControladorAula():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_aula = TelaAula()
    
    def acessar_python(self):
        aula_python = ['Python', 'O Python é uma linguagem de programação pipipipopopo', 'https://link.conteudo.python']
        for c in range (len(aula_python)):
            self.__tela_aula.mostra_aulas(aula_python[c])
        
    def retornar_curso(self):
        self.__controlador_sistema.ver_curso()

    def abre_tela(self):
        lista_opcoes = {1: self.acessar_python, 0:self.retornar_curso}
    
        while True:
            lista_opcoes[self.__tela_aula.tela_opcoes()]()