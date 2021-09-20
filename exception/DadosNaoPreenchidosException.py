from exception.Exception import Exception

class DadosNaoPreenchidosException(Exception):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, "Preencha todos os campos")
