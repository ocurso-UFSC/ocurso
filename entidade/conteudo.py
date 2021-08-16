class Conteudo:
    def __init__(
            self,
            descricao_conteudo: str,
            link_conteudo: str,):
        self.__descricao_conteudo = descricao_conteudo
        self.__link_conteudo = link_conteudo

    @property
    def descricao_conteudo(self):
        return self.__descricao_conteudo

    @property
    def link_conteudo(self):
        return self.__link_conteudo

    @descricao_conteudo.setter
    def descricao_conteudo(self, descricao_conteudo):
        self.__descricao_conteudo = descricao_conteudo

    @link_conteudo.setter
    def link_conteudo(self, link_conteudo):
        self.__link_conteudo = link_conteudo
