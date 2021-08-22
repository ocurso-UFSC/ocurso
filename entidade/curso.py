class Curso:
  def __init__(
      self,
      nome_do_curso: str,
      descricao: str,
      quantidade_horas: str,
      aula: str = None,
      ):

    self.__nome_do_curso = nome_do_curso
    self.__descricao = descricao
    self.__quantidade_horas = quantidade_horas
    self.__aula = aula
    self.__avaliacao = []


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
  def avaliacao(self):
    return self.__avaliacao

  @nome_do_curso.setter
  def nome_do_curso(self, nome_do_curso):
    self.__nome_do_curso = nome_do_curso

  @descricao.setter
  def descricao(self, descricao):
    self.__descricao = descricao

  @quantidade_horas.setter
  def quantidade_horas(self, quantidade_horas):
    self.__quantidade_horas = quantidade_horas

  @aula.setter
  def aula(self, aula):
    self.__aula = aula

  @aula.setter
  def lista_aulas(self, aula):
    self.__aula = aula