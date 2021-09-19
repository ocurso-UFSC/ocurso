class Aula:
  def __init__(
      self,
      # codigo: int,
      descricao_aula: str,
      link_aula: str):

    # self.__codigo = codigo
    self.__descricao_aula = descricao_aula
    self.__link_aula = link_aula

  # @property
  # def codigo(self):
  #   return self.__codigo

  @property
  def descricao_aula(self):
    return self.__descricao_aula

  @property
  def link_aula(self):
    return self.__link_aula

  # @codigo.setter
  # def codigo(self, codigo):
  #   self.__codigo = codigo

  @descricao_aula.setter
  def descricao_aula(self, descricao_aula):
    self.__descricao_aula = descricao_aula

  @link_aula.setter
  def link_aula(self, link_aula):
    self.__link_aula = link_aula
