from limite.TelaProgresso import TelaProgresso
from entidade.progresso import Progresso


class ControladorProgresso():
  def __init__(self, controlador_sistema):
    self.__progressos = []
    self.__tela_progresso = TelaProgresso()
    self.__controlador_sistema = controlador_sistema

  def pega_progresso_por_email(self, email: str):
    for progresso in self.__progressos:
      if (progresso.usuario.email == email):
        return progresso
    return None

  
  
