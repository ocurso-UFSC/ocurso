class Alternativa:
  def __init__(
      self,
      index: str,
      descricao_alternativa: str,):

    self.__index = index
    self.__descricao_alternativa = descricao_alternativa

  @property
  def index(self):
    return self.__index

  @property
  def descricao_alternativa(self):
    return self.__descricao_alternativa

  @index.setter
  def index(self, index):
    self.__index = index

  @descricao_alternativa.setter
  def descricao_alternativa(self, descricao_alternativa):
    self.__descricao_alternativa = descricao_alternativa
