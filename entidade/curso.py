from usuario import Usuario
from avaliacao import Avaliacao
from aula import Aula


class Curso:
  def __init__(
      self,
      nome_do_curso: str,
      descricao: str,
      quantidade_horas: str,
      aula: Aula,
      inscritos: list,
      aprovados: list,
      lista_aulas: list,
      ):

    self.__nome_do_curso = nome_do_curso
    self.__descricao = descricao
    self.__quantidade_horas = quantidade_horas
    self.__aula = aula
    self.__inscritos = inscritos
    self.__aprovados = aprovados
    self.__lista_aulas = lista_aulas

  @property
  def nome_do_curso(self):
    return self.__nome_do_curso

  @property
  def descricao(self):
    return self.__descricao

  @property
  def quantidade_horas(self):
    return self.__quantidade_horas

  @property
  def aula(self):
    return self.__aula

  @property
  def inscritos(self):
    return self.__inscritos

  @property
  def aprovados(self):
    return self.__aprovados

  @property
  def lista_aulas(self):
    return self.__lista_aulas

  @nome_do_curso.setter
  def nome_do_curso(self, nome_do_curso):
    self.__nome_do_curso = nome_do_curso

  @descricao.setter
  def nome(self, descricao):
    self.__descricao = descricao

  @quantidade_horas.setter
  def quantidade_horas(self, quantidade_horas):
    self.__quantidade_horas = quantidade_horas

  @aula.setter
  def aula(self, aula):
    self.__aula = aula

  @inscritos.setter
  def nome(self, inscritos):
    self.__inscritos = inscritos

  @aprovados.setter
  def aprovados(self, aprovados):
    self.__aprovados = aprovados

  @lista_aulas.setter
  def lista_aulas(self, lista_aulas):
    self.__lista_aulas = lista_aulas


  def gerar_certificar(self):
    # fazer ainda
    pass