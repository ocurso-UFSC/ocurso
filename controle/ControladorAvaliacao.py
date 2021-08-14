from limite.TelaAvaliacao import TelaAvaliacao

class ControladorAvaliacao():
  def __init__(self, controlador_sistema):
    self.__tela_avaliacao = TelaAvaliacao
    self.__avaliacoes = ['Python', 'JavaScript']

  def listar_avaliacoes(self):
    for avaliacao in self.__avaliacoes:
      self.__tela_avaliacao.mostra_avaliacoes(self.__avaliacoes[avaliacao])
