from usuario import Usuario

class Aula:
    def __init__(
                self,
                classe_usuario: Usuario.is_admin,
                numero_aula: int,
                conteudos: dict,
                concluidos: int):
        self.__classe_usuario = classe_usuario
        self.__numero_aula = numero_aula
        self.__conteudos = conteudos
        self.__concluidos = concluidos

    @property
    def classe_usuario(self):
        return self.__classe_usuario

    @property
    def numero_aula(self):
        return self.__numero_aula

    @property
    def conteudos(self):
        return self.__conteudos

    @property
    def concluidos(self):
        return self.__concluidos

    @classe_usuario.setter
    def classe_usuario(self, classe_usuario):
        self.__classe_usuario = classe_usuario

    @numero_aula.setter
    def numero_aula(self, numero_aula):
        self.__numero_aula = numero_aula

    @conteudos.setter
    def conteudos(self, conteudos):
        self.__conteudos = conteudos

    @concluidos.setter
    def concluidos(self, concluidos):
        self.__concluidos = concluidos

    def adicionar_conteudo(self):
        ...

    def remover_conteudo(self):
        ...
