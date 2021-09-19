from dao.abstract_dao import DAO
from entidade.progresso import Progresso

class progressoDAO(DAO):
  def __init__(self):
    super().__init__('progressos.pkl')
  
  def add(self, progresso: Progresso):
    if (progresso is not None) and (isinstance(progresso.codigo, int)) \
        and isinstance(progresso, Progresso):
      super().add(progresso.codigo, progresso)

  def get(self, key: str):
    if isinstance(key, str):
      return super().get(key)

  def get_all(self):
    return super().get_all()

  def update(self):
    return super().update()

  def remove(self, key: int):
    if isinstance(key, int):
      return super().remove(key)