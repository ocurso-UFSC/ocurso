class Alternativa:
    def __init__(self,
                index: str,
                descricao_alternativa: str,
                status_alternativa: bool):
            self.__index = index
            self.__descricao_alternativa = descricao_alternativa
            self.__status_alternativa = status_alternativa

    @property
    def index(self):
        return self.__index

    @property
    def descricao_alternativa(self):
        return self.__descricao_alternativa

    @property
    def status_alternativa(self):
        return self.__status_alternativa

    @index.setter
    def index(self, index):
        self.__index = index

    @descricao_alternativa.setter
    def descricao_alternativa(self, descricao_alternativa):
        self.__descricao_alternativa = descricao_alternativa

    @status_alternativa.setter
    def status_alternativa(self, status_alternativa):
        self.__status_alternativa = status_alternativa
