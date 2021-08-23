class Aula:
  def __init__(
      self,
      descricao_aula: str,
      link_aula: str,
      ):

    self.descricao_aula = descricao_aula
    self.link_aula = link_aula

  @property
  def descricao_aula(self):
    return self.descricao_aula

  @property
  def link_aula(self):
    return self.link_aula

  @descricao_aula.setter
  def descricao_aula(self, descricao_aula):
    self.descricao_aula = descricao_aula

  @link_aula.setter
  def link_aula(self, link_aula):
    self.link_aula = link_aula
