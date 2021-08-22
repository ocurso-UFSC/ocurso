from entidade.alternativa import Alternativa

class Questao:
  def __init__(
      self,
      descricao_questao: str,
      alternativa: Alternativa,
      alternativa_correta: str):

    self.__descricao_questao = descricao_questao
    self.__alternativa = alternativa
    self.__lista_alternativas = []
    self.__lista_alternativas.append(alternativa)
    self.__alternativa_correta = alternativa_correta

  @property
  def descricao_questao(self):
    return self.__descricao_questao

  @property
  def alternativa(self):
    return self.__alternativa

  @property
  def alternativa_correta(self):
    return self.__alternativa_correta

  @descricao_questao.setter
  def descricao_questao(self, descricao_questao):
    self.__descricao_questao = descricao_questao

  @alternativa.setter
  def alternativa(self, alternativa):
    self.__alternativa = alternativa

  @alternativa_correta.setter
  def alternativa_correta(self, alternativa_correta):
    self.__alternativa_correta = alternativa_correta
