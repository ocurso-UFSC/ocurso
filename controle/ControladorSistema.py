from limite.TelaSistema import TelaSistema
from controle.ControladorCurso import ControladorCurso
from controle.ControladorQuestao import ControladorQuestao
from controle.ControladorUsuario import ControladorUsuario
from controle.ControladorLogin import ControladorLogin
from controle.ControladorAula import ControladorAula
from controle.ControladorProgresso import ControladorProgresso

class ControladorSistema:
    def __init__(self, usuario_logado = None):
        self.__usuario_logado = usuario_logado
        self.__tela_sistema = TelaSistema()
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_questao = ControladorQuestao(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_login = ControladorLogin(self)
        self.__controlador_aula = ControladorAula(self)
        self.__controlador_progresso = ControladorProgresso(self)

   
    @property
    def controlador_curso(self):
        return self.__controlador_curso

    @property
    def controlador_questao(self):
        return self.__controlador_questao

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario

    @property
    def controlador_progresso(self):
        return self.__controlador_progresso

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, usuario_logado):
        self.__usuario_logado = usuario_logado

    def inicializa_sistema(self):
        if self.__usuario_logado == None:
            self.__controlador_login.abre_tela()
        else:
            self.abre_tela()

    def usuario(self):
        self.__controlador_usuario.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()

    def ver_curso(self):
        self.__controlador_curso.abre_tela()

    def inclui_questao(self):
        self.__controlador_questao.abre_tela()
    
    def abre_aulas(self):
        self.__controlador_aula.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_mensagem("Adios")
        exit(0)

    def deslogar(self):
        self.__tela_sistema.mostra_mensagem("Usuario Deslogado")
        self.usuario_logado = None
        self.__controlador_login.abre_tela()

    def automatico(self):
        # cria usuarios
        
        dados_usuario = {"nome": "Joao", "email": "joao@gmail.com", "senha": "123", "adm": False}
        self.__controlador_usuario.criar_usuario(dados_usuario)

        dados_usuario = {"nome": "Ricardo", "email": "ricardo@gmail.com", "senha": "123", "adm": False}
        self.__controlador_usuario.criar_usuario(dados_usuario)


        # cria cursos
        dados_curso = {"nome_do_curso": "python", "descricao": "Vc vai aprender Python",
                "quantidade_horas": "9"}
        self.__controlador_curso.cadastrar_curso(dados_curso)
        
        dados_curso = {"nome_do_curso": "django", "descricao": "Vc vai aprender Django",
                "quantidade_horas": "3"}
        self.__controlador_curso.cadastrar_curso(dados_curso)


    def progresso(self):
        self.__controlador_progresso.abre_tela()

    def abre_tela(self):
        self.__tela_sistema.mostra_mensagem("\n")
        lista_opcoes = {1: self.usuario,  2: self.inclui_questao, 3: self.ver_curso, 4: self.progresso, 9: self.automatico, 0: self.deslogar}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()