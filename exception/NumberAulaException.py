from exception.Exception import Exception

class NumberAulaException(Exception):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, "Horas deve ser um valor inteiro")