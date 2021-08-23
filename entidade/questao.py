class Questao:
  def __init__(
      self,
      descricao_questao: str,
      lista_alternativas: list,
      alternativa_correta: str):

    self.__descricao_questao = descricao_questao
    self.__lista_alternativas = lista_alternativas
    self.__alternativa_correta = alternativa_correta

  @property
  def descricao_questao(self):
    return self.__descricao_questao

  @property
  def lista_alternativas(self):
    return self.__lista_alternativas

  @property
  def alternativa_correta(self):
    return self.__alternativa_correta

  @descricao_questao.setter
  def descricao_questao(self, descricao_questao):
    self.__descricao_questao = descricao_questao

  @lista_alternativas.setter
  def lista_alternativas(self, lista_alternativas):
    self.__lista_alternativas = lista_alternativas

  @alternativa_correta.setter
  def alternativa_correta(self, alternativa_correta):
    self.__alternativa_correta = alternativa_correta
