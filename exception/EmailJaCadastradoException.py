from exception.Exception import Exception

class EmailJaCadastradoException(Exception):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema, "Email já cadastrado.")
