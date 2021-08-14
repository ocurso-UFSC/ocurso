from alternativa import Alternativa

class Questao:
    def __init__(self,
                numero_questao: int,
                descricao_questao: str,
                alternativa: Alternativa,
                alternativas: list,
                acerto: int):
            self.__numero_questao = numero_questao
            self.__descricao_questao = descricao_questao
            self.__alternativa = alternativa
            self.__alternativas = alternativas
            self.__alternativas.append(alternativa)
            self.__acerto = acerto      #talvez esse atributo seja do controlador, e não da classe "Questao"

    @property
    def numero_questao(self):
        return self.__numero_questao

    @property
    def descricao_questao(self):
        return self.__descricao_questao

    @property
    def alternativa(self):
        return self.__alternativa

    @property
    def alternativas(self):
        return self.__alternativas

    @property
    def acerto(self):
        return self.__acerto

    @numero_questao.setter
    def numero_questao(self, numero_questao):
        self.__numero_questao = numero_questao

    @descricao_questao.setter
    def descricao_questao(self, descricao_questao):
        self.__descricao_questao = descricao_questao

    @alternativa.setter
    def alternativa(self, alternativa):
        self.__alternativa = alternativa

    @alternativas.setter
    def alternativas(self, alternativas):
        self.__alternativas = alternativas

    @acerto.setter
    def acerto(self, acerto):
        self.__acerto = acerto

    def editar_descricao(self, descricao_questao):
        ...

    def adicionar_alternativa(self, alternativas):
        ... #tanto aqui quanto nas def's abaixo terá um "if usuario == adm:" para realizar o procedimento
            #talvez seja necessário colocar essas def's na classe "Alternativa" mesmo

    def remover_alternativa(self, alternativas):
        ...

    def definir_alternativa_correta(self, alternativa):
        ...
