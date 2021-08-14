from entidade.usuario import Usuario
from entidade.conteudo import Conteudo

class Aula:
    def __init__(
                self,
                numero_aula: int,
                conteudo: Conteudo,
                lista_conteudos: dict,
                concluidos: int):
        self.__numero_aula = numero_aula
        self.__conteudo = conteudo
        self.__lista_conteudos = lista_conteudos
        self.__concluidos = concluidos

    @property
    def numero_aula(self):
        return self.__numero_aula

    @property
    def conteudo(self):
        return self.__conteudo

    @property
    def lista_conteudos(self):
        return self.__lista_conteudos

    @property
    def concluidos(self):
        return self.__concluidos

    @numero_aula.setter
    def numero_aula(self, numero_aula):
        self.__numero_aula = numero_aula

    @conteudo.setter
    def conteudo(self, conteudo):
        self.__conteudo = conteudo

    @lista_conteudos.setter
    def lista_conteudos(self, lista_conteudos):
        self.__lista_conteudos = lista_conteudos

    @concluidos.setter
    def concluidos(self, concluidos):
        self.__concluidos = concluidos
