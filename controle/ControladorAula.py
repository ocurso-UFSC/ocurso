import PySimpleGUI as sg
from limite.TelaAula import TelaAula
from entidade.aula import Aula

class ControladorAula():
  def __init__(self, controlador_sistema):
    self.__controlador_sistema = controlador_sistema
    self.__tela_aula = TelaAula()
    self.__aula = Aula
  
  def listar_aulas(self):
    self.__tela_aula.limpar_lista_aulas()
    curso = self.__controlador_sistema.controlador_curso._ControladorCurso__curso_escolhido
    for aula in curso._Curso__lista_aulas:
      numero_aula = curso._Curso__lista_aulas.index(aula) + 1
      descricao_aula = aula._Aula__descricao_aula
      self.__tela_aula.lista_aulas(numero_aula, descricao_aula)

  def mostra_aulas(self):
    self.__tela_aula.close()
    curso = self.__controlador_sistema.controlador_curso._ControladorCurso__curso_escolhido
    progresso = self.__controlador_sistema.controlador_progresso.progresso_por_curso_e_usuario(curso.codigo)
    aulas_restantes = len(curso._Curso__lista_aulas) - progresso.ultima_aula
    if aulas_restantes <= 0:
      see_again = self.__tela_aula.open_pergunta()
      if see_again == 'yes':
        progresso.ultima_aula = 0
      self.__tela_aula.close_mexe_na_aula()


    for _ in range(aulas_restantes):
      aula = curso.lista_aulas[progresso.ultima_aula]
      continuar = self.__tela_aula.open_mostra_aulas(progresso.ultima_aula + 1, aula._Aula__descricao_aula, aula._Aula__link_aula)
      if continuar == 'S':
        progresso.ultima_aula += 1
      if continuar == 'N':
        break
      if progresso.ultima_aula == len(curso._Curso__lista_aulas):
        self.__tela_aula.open_mensagem('Parabéns!', 'Você concluiu as aulas deste curso!')
        self.__tela_aula.close_mexe_na_aula()
      self.__tela_aula.close_pega_dados_aula()
    self.listar_aulas()

  def cadastra_aula(self, dados):
    aula = Aula(dados['descricao_aula'], dados['link_aula'])
    self.__controlador_sistema.controlador_curso.adicionar_aula(aula)

  def adiciona_aula(self):
    self.__tela_aula.close()
    dados_aula = self.__tela_aula.open_pega_dados_aula()
    descricao_aula = dados_aula['descricao_aula']
    link_aula = dados_aula['link_aula']
    aula = self.__aula(descricao_aula, link_aula)
    self.__controlador_sistema.controlador_curso.adicionar_aula(aula)
    self.__tela_aula.close_pega_dados_aula()
    self.listar_aulas()

  def altera_aula(self):
    self.__tela_aula.close()
    numero_aula = self.__tela_aula.open_mexe_na_aula('Alterar aulas')
    dados_aula = self.__tela_aula.open_pega_dados_aula()
    descricao_aula = dados_aula['descricao_aula']
    link_aula = dados_aula['link_aula']
    aula = self.__aula(descricao_aula, link_aula)
    self.__controlador_sistema.controlador_curso.alterar_aula(numero_aula, aula)
    self.__tela_aula.close_mexe_na_aula()
    self.__tela_aula.close_pega_dados_aula()
    self.listar_aulas()

  def exclui_aula(self):
    self.__tela_aula.close()
    numero_aula = self.__tela_aula.open_mexe_na_aula('Excluir aulas')
    self.__controlador_sistema.controlador_curso.remover_aula(numero_aula)
    self.__tela_aula.close_mexe_na_aula()
    self.listar_aulas()

  def retornar(self):
    self.__tela_aula.close()
    self.__controlador_sistema.ver_curso()

  def abre_tela(self):
    usuario_logado = self.__controlador_sistema._ControladorSistema__usuario_logado
    adm = usuario_logado._Usuario__adm
    self.listar_aulas()
    lista_opcoes = {1:self.mostra_aulas, 2:self.adiciona_aula, 3:self.altera_aula, 4:self.exclui_aula, 0:self.retornar}

    while True:
      lista_opcoes[self.__tela_aula.open(adm)]()
