from dao.abstract_dao import DAO
from entidade.aula import Aula

class aulaDAO(DAO):
  def __init__(self):
    super().__init__('aulas.pkl')
  
  def add(self, aula:     Aula ):
    if (aula is not None) and (isinstance(aula.codigo, int)) \
        and isinstance(aula,     Aula ):
      super().add(aula.codigo, aula)

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
