class Conteudo:
    def __init__(
            self,
            numero_conteudo: int,
            descricao_conteudo: str,
            link_conteudo: str,
            checkbox: bool):
        self.__numero_conteudo = numero_conteudo
        self.__descricao_conteudo = descricao_conteudo
        self.__link_conteudo = link_conteudo
        self.__checkbox = checkbox

    @property
    def numero_conteudo(self):
        return self.__numero_conteudo

    @property
    def descricao_conteudo(self):
        return self.__descricao_conteudo

    @property
    def link_conteudo(self):
        return self.__link_conteudo

    @property
    def checkbox(self):
        return self.__checkbox

    @numero_conteudo.setter
    def numero_conteudo(self, numero_conteudo):
        self.__numero_conteudo = numero_conteudo

    @descricao_conteudo.setter
    def descricao_conteudo(self, descricao_conteudo):
        self.__descricao_conteudo = descricao_conteudo

    @link_conteudo.setter
    def link_conteudo(self, link_conteudo):
        self.__link_conteudo = link_conteudo

    @checkbox.setter
    def checkbox(self, checkbox):
        self.__checkbox = checkbox