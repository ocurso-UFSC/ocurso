# from progresso import Progresso
# from curso import Curso


class Usuario:
  def __init__(
      self,
      nome: str,
      email: str,
      senha: str,
      adm: bool,
      notas: list = [],
      progresso: list = []):

    self.__nome = nome
    self.__email = email
    self.__senha = senha
    self.__adm = adm
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
  def adm(self):
    return self.__adm

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
  def email(self, email):
    self.__email = email

  @senha.setter
  def senha(self, senha):
    self.__senha = senha

  @notas.setter
  def notas(self, notas):
    self.__notas = notas

  @progresso.setter
  def progresso(self, progresso):
    self.__progresso = progresso