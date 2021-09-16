from limite.TelaSistema import TelaSistema
from controle.ControladorCurso import ControladorCurso
from controle.ControladorQuestao import ControladorQuestao
from controle.ControladorUsuario import ControladorUsuario
from controle.ControladorLogin import ControladorLogin
from controle.ControladorAula import ControladorAula
from controle.ControladorProgresso import ControladorProgresso

class ControladorSistema:
    __instance = None

    def __init__(self, usuario_logado = None):
        self.__tela_sistema = TelaSistema()
        self.__usuario_logado = usuario_logado
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_questao = ControladorQuestao(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_login = ControladorLogin(self)
        self.__controlador_aula = ControladorAula(self)
        self.__controlador_progresso = ControladorProgresso(self)
    
    def __new__(cls):
        if ControladorSistema.__instance is None:
            ControladorSistema.__instance = object.__new__(cls)
        return ControladorSistema.__instance

    @property
    def controlador_curso(self):
        return self.__controlador_curso

    @property
    def controlador_aula(self):
        return self.__controlador_aula

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

    def ver_curso(self):
        self.__tela_sistema.close()
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

        # cria progresso usuario
        curso = self.__controlador_curso.pega_curso_por_nome("python")
        self.__controlador_progresso.cria_progresso(curso,self.__usuario_logado)

        curso = self.__controlador_curso.pega_curso_por_nome("django")
        self.__controlador_progresso.cria_progresso(curso,self.__usuario_logado)

        # adiciona algumas aulas
        
        # # aula 1 = python
        # dados_aula = {"descricao_aula": "Lorem ipsum lorem", "link_aula": "www.aula_01_python.com"}
        # self.__controlador_aula.cadastra_aula("python", dados_aula)

        # # aula 2 = python
        # dados_aula = {"descricao_aula": "Lorem ipsum lorem", "link_aula": "www.aula_02_python.com"}
        # self.__controlador_aula.cadastra_aula("python", dados_aula)

        # # aula 3 = python
        # dados_aula = {"descricao_aula": "Lorem ipsum lorem", "link_aula": "www.aula_03_python.com"}
        # self.__controlador_aula.cadastra_aula("python", dados_aula)

        # # aula 4 = python
        # dados_aula = {"descricao_aula": "Lorem ipsum lorem", "link_aula": "www.aula_04_python.com"}
        # self.__controlador_aula.cadastra_aula("python", dados_aula)

        # # aula 5 = python
        # dados_aula = {"descricao_aula": "Lorem ipsum lorem", "link_aula": "www.aula_05_python.com"}
        # self.__controlador_aula.cadastra_aula("python", dados_aula)

        # # aula 1 = django
        # dados_aula = {"descricao_aula": "Lorem ipsum lorem", "link_aula": "www.aula_01_django.com"}
        # self.__controlador_aula.cadastra_aula("django", dados_aula)

        # # aula 2 = django
        # dados_aula = {"descricao_aula": "Lorem ipsum lorem", "link_aula": "www.aula_02_django.com"}
        # self.__controlador_aula.cadastra_aula("django", dados_aula)


        # Questao curso
        infos_questao = {'descricao_questao':'Qual é a certa?', 'alternativa_correta': 'a'}
        desc_alternativas = ["Lorem ipsum, lorem ipsum", "Ipsum lorem, ipsum lorem"]
        self.__controlador_questao.cadastra_questao_aut("python", infos_questao, desc_alternativas)

    def progresso(self):
        self.__controlador_progresso.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.usuario, 2: self.ver_curso, 3: self.progresso, 9: self.automatico, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.open()
            
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
        self.__tela_sistema.close()
