from dao.abstract_dao import DAO
from entidade.conteudo import Conteudo

class conteudoDAO(DAO):
  def __init__(self):
    super().__init__('conteudos.pkl')
  
  def add(self, conteudo:     Conteudo ):
    if (conteudo is not None) and (isinstance(conteudo.codigo, int)) \
        and isinstance(conteudo,     Conteudo ):
      super().add(conteudo.codigo, conteudo)

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