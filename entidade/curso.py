class Curso:
  def __init__(
      self,
      codigo: int,
      nome_do_curso: str,
      descricao: str,
      quantidade_horas: str
      ):

    self.__codigo = codigo
    self.__nome_do_curso = nome_do_curso
    self.__descricao = descricao
    self.__quantidade_horas = quantidade_horas
    self.__lista_aulas = []
    self.__avaliacao = []

  @property
  def codigo(self):
    return self.__codigo

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
  def lista_aulas(self):
    return self.__lista_aulas
  
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

  @lista_aulas.setter
  def lista_aulas(self, lista_aulas):
    self.__lista_aulas = lista_aulas

  def adiciona_aula(self, aula):
    self.__lista_aulas.append(aula)