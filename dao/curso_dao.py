from dao.abstract_dao import DAO
from entidade.curso import Curso

class cursoDAO(DAO):
  def __init__(self):
    super().__init__('cursos.pkl')
  
  def add(self, curso: Curso):
    if (curso is not None) and (isinstance(curso.codigo, int)) \
        and isinstance(curso, Curso):
      super().add(curso.codigo, curso)

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