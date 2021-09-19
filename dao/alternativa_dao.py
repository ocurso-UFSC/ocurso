from dao.abstract_dao import DAO
from entidade.alternativa import Alternativa

class alternativaDAO(DAO):
  def __init__(self):
    super().__init__('alternativas.pkl')
  
  def add(self, alternativa:     Alternativa ):
    if (alternativa is not None) and (isinstance(alternativa.codigo, int)) \
        and isinstance(alternativa,     Alternativa ):
      super().add(alternativa.codigo, alternativa)

  def get(self, key: str):
    if isinstance(key, str):
      return super().get(key)

  def get_all(self):
    return super().get_all()

  def update(self):
    return super().get_all()

  def remove(self, key: str):
    if isinstance(key, str):
      return super().remove(key)