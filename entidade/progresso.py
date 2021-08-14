from usuario import Usuario
from curso import Curso
from avaliacao import Avaliacao
    
class Progresso:
  def __init__(
      self,
      usuario: Usuario,
      aulas_concluidas: Curso,
      nota: Avaliacao):

    self.__usuario = usuario
    self.__aulas_concluidas = aulas_concluidas
    self.__nota = nota

  @property
  def usuario(self):
    return self.__usuario

  @property
  def aulas_concluidas(self):
    return self.__aulas_concluidas

  @property
  def nota(self):
    return self.__nota

  @usuario.setter
  def usuario(self, usuario):
    self.__usuario = usuario

  @aulas_concluidas.setter
  def nome(self, aulas_concluidas):
    self.__aulas_concluidas = aulas_concluidas

  @nota.setter
  def nome(self, nota):
    self.__nota = nota
