from exception.Exception import Exception

class SenhasNaoCorrespondemException(Exception):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, "Senhas não correspondem")
