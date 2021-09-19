from dao.abstract_dao import DAO
from entidade.questao import Questao

class questaoDAO(DAO):
  def __init__(self):
    super().__init__('questaos.pkl')

  def add(self, questao: Questao):
    if (questao is not None) and (isinstance(questao.codigo, int)) \
        and isinstance(questao, Questao):
      super().add(questao.codigo, questao)

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
