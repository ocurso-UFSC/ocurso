from dao.abstract_dao import DAO
from entidade.usuario import Usuario

class usuarioDAO(DAO):
  def __init__(self):
    super().__init__('usuarios.pkl')
  
  def add(self, usuario: Usuario):
    if (usuario is not None) and (isinstance(usuario.email, str)) \
        and isinstance(usuario, Usuario):
      super().add(usuario.email, usuario)

  def get(self, key: str):
    if isinstance(key, str):
      return super().get(key)

  def get_all(self):
    return super().get_all()

  def update(self):
    return super().update()

  def remove(self, key: str):
    if isinstance(key, str):
      return super().remove(key)
