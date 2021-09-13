    
class Progresso:
  def __init__(
      self,
      usuario: object,
      curso: object,
      ultima_aula: int = 0,
      nota: float = None):

    self.__usuario = usuario
    self.__curso = curso
    self.__ultima_aula = ultima_aula
    self.__nota = nota

  @property
  def usuario(self):
    return self.__usuario

  @property
  def curso(self):
    return self.__curso
  
  @property
  def ultima_aula(self):
    return self.__ultima_aula

  @property
  def nota(self):
    return self.__nota
  
  @usuario.setter
  def usuario(self, usuario):
    self.__usuario = usuario

  @curso.setter
  def curso(self, curso):
    self.__curso = curso

  @ultima_aula.setter
  def ultima_aula(self, ultima_aula):
    self.__ultima_aula = ultima_aula

  @nota.setter
  def nota(self, nota):
    self.__nota = nota