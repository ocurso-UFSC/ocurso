from limite.TelaAula import TelaAula
from entidade.aula import Aula

class ControladorAula():
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__tela_aula = TelaAula()
    # self.__ultimas_aulas = {}         # este dict possui o nome do curso e a aula em que o usuário parou. Deve ser atribuido ao usuario "curso | ultima aula parada"
    self.__aula = Aula

  def mostra_aulas(self):
    nome_curso = self.__tela_aula.nome_curso()
    curso = self.__controlador_sistema.controlador_curso.pega_curso_por_nome(nome_curso)
    # print("Curso", curso) [ACHOU]
    progresso = self.__controlador_sistema.controlador_progresso.progresso_por_curso_e_usuario(curso)
    print("progresso", progresso)
    aulas_restantes = len(curso._Curso__lista_aulas) - progresso.ultima_aula

    for c in range(aulas_restantes):
      aula = curso.lista_aulas[progresso.ultima_aula]
      self.__tela_aula.mostra_aulas(progresso.ultima_aula + 1, aula._Aula__descricao_aula, aula._Aula__link_aula)
      progresso.ultima_aula += 1 # talvez precisa repetir
      continuar = self.__tela_aula.continuar_aula()
      if continuar == 'N':
        break

      if progresso.ultima_aula == len(curso._Curso__lista_aulas):
        self.__tela_aula.mostra_mensagem('\nParabéns! Você concluiu as aulas deste curso.')

  def cadastra_aula(self, nome_curso, dados):
    aula = Aula(dados['descricao_aula'], dados['link_aula'])
    self.__controlador_sistema.controlador_curso.adicionar_aula(nome_curso, aula)

  def adiciona_aula(self):                                     #adicionando aula
    nome_curso = self.__tela_aula.nome_curso()
    dados_aula = self.__tela_aula.pega_dados_aula()
    descricao_aula = dados_aula['descricao_aula']
    link_aula = dados_aula['link_aula']
    aula = self.__aula(descricao_aula, link_aula)
    self.__controlador_sistema.controlador_curso.adicionar_aula(nome_curso, aula)

  def altera_aula(self):
    nome_curso = self.__tela_aula.nome_curso()
    numero_aula = self.__tela_aula.mexe_na_aula('Qual aula você deseja alterar? ')
    dados_aula = self.__tela_aula.pega_dados_aula()
    descricao_aula = dados_aula['descricao_aula']
    link_aula = dados_aula['link_aula']
    aula = self.__aula(descricao_aula, link_aula)
    self.__controlador_sistema.controlador_curso.alterar_aula(nome_curso, numero_aula, aula)

  def exclui_aula(self):
    nome_curso = self.__tela_aula.nome_curso()
    numero_aula = self.__tela_aula.mexe_na_aula('Qual aula você deseja excluir? ')
    self.__controlador_sistema.controlador_curso.remover_aula(nome_curso, numero_aula)

  def retornar(self):
    self.__controlador_sistema.abre_tela()
  
  def abre_tela(self):
    lista_opcoes = {1:self.mostra_aulas, 2:self.adiciona_aula, 3:self.altera_aula, 4:self.exclui_aula, 0:self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_aula.tela_opcoes()]()
