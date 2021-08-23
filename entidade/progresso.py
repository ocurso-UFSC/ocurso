    
class Progresso:
  def __init__(
      self,
      usuario: object,
      curso: object,
      aulas_concluidas: list = [],
      nota: dict = {}):

    self.__usuario = usuario
    self.__curso = curso
    self.__aulas_concluidas = aulas_concluidas
    self.__nota = nota

  @property
  def usuario(self):
    return self.__usuario

  @property
  def curso(self):
    return self.__curso
  
  @property
  def aulas_concluidas(self):
    return self.__aulas_concluidas

  @property
  def nota(self):
    return self.__nota
  
  @usuario.setter
  def usuario(self, usuario):
    self.__usuario = usuario

  @curso.setter
  def curso(self, curso):
    self.__curso = curso

  @aulas_concluidas.setter
  def aulas_concluidas(self, aulas_concluidas):
    self.__aulas_concluidas = aulas_concluidas

  @nota.setter
  def nota(self, nota):
    self.__nota = nota

  def gerar_certificado(self):
    return ("Usuario", self.usuario.nome, "Completou o curso", self.curso.nome_do_curso,
            "com uma carga horária de ", self.curso.quantidade_horas)