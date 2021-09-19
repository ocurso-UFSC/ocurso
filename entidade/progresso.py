    
class Progresso:
  def __init__(
      self,
      codigo: int,
      usuario_cod: str,
      curso_cod: int,
      ultima_aula: int = 0,
      nota: float = None):

    self.__codigo = codigo
    self.__usuario_cod = usuario_cod
    self.__curso_cod = curso_cod
    self.__ultima_aula = ultima_aula
    self.__nota = nota

  @property
  def codigo(self):
    return self.__codigo

  @property
  def usuario_cod(self):
    return self.__usuario_cod

  @property
  def curso_cod(self):
    return self.__curso_cod
  
  @property
  def ultima_aula(self):
    return self.__ultima_aula

  @property
  def nota(self):
    return self.__nota
  
  @usuario_cod.setter
  def usuario_cod(self, usuario_cod):
    self.__usuario_cod = usuario_cod

  @curso_cod.setter
  def curso_cod(self, curso_cod):
    self.__curso_cod = curso_cod

  @ultima_aula.setter
  def ultima_aula(self, ultima_aula):
    self.__ultima_aula = ultima_aula

  @nota.setter
  def nota(self, nota):
    self.__nota = nota