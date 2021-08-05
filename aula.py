class Aula:
    def __init__(
                self,
                numero_aula: int,
                conteudos: list,
                checkbox: bool):
        self.__numero_aula = numero_aula
        self.__conteudos = conteudos
        self.__checkbox = checkbox

    @property
    def numero_aula(self):
        return self.__numero_aula

    @property
    def conteudos(self):
        return self.__conteudos

    @property
    def checkbox(self):
        return self.__checkbox

    @numero_aula.setter
    def numero_aula(self, numero_aula):
        self.__numero_aula = numero_aula

    @conteudos.setter
    def conteudos(self, conteudos):
        self.__conteudos = conteudos

    @checkbox.setter
    def checkbox(self, checkbox):
        self.__checkbox = checkbox

    def adicionar_conteudo(self):
        ...

    def remover_conteudo(self):
        ...
