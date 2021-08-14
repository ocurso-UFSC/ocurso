from progresso import Progresso
from curso import Curso


class Usuario:
    def __init__(
                self,
                nome: str,
                email: str,
                senha: str,
                is_admin: bool,
                notas: list = [],
                progresso: list = []):

        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__notas = notas
        self.__progresso = progresso


    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def is_admin(self):
        return self.__is_admin

    @property
    def notas(self):
        return self.__notas

    @property
    def progresso(self):
        return self.__progresso

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @email.setter
    def nome(self, email):
        self.__email = email

    @senha.setter
    def nome(self, senha):
        self.__senha = senha

    @is_admin.setter
    def nome(self, is_admin):
        self.__is_admin = is_admin

    @notas.setter
    def nome(self, notas):
        self.__notas = notas

    @progresso.setter
    def nome(self, progresso):
        self.__progresso = progresso