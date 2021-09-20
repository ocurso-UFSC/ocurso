class Exception():
  def __init__(self, controlador_sistema, mensagem):
    controlador_sistema.tela_sistema.mostra_mensagem(mensagem)