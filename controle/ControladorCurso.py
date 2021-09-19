from os import error
from limite.telaCurso import TelaCurso
from entidade.curso import Curso
from dao.curso_dao import cursoDAO

class ControladorCurso():
  def __init__(self, controlador_sistema):
    self.__dao = cursoDAO()
    self.__curso_escolhido = Curso
    self.__tela_curso = TelaCurso()
    self.__controlador_sistema = controlador_sistema

  @property
  def lista_cursos(self):
    return self.__dao.get_all()

  def get_next_key(self):
    all = list(self.__dao.get_all())
    return all[-1].codigo + 1

  def get_curso_por_key(self, key):
    return self.__dao.get(key)

  def pega_curso_por_nome(self, nome: str = None):
    for curso in self.lista_cursos:
      if (curso.nome_do_curso == nome):
        return curso
    return None

  def busca_curso_escolhido(self):
    nome_curso = self.__curso_escolhido._Curso__nome_do_curso
    return self.pega_curso_por_nome(nome_curso)

  def incluir_curso(self):
    dados_curso = self.__tela_curso.pega_dados_curso()
    
    codigo = self.get_next_key()
    curso = Curso(codigo, dados_curso["nome_do_curso"], dados_curso["descricao"], 
                    dados_curso["quantidade_horas"])
    
    self.__dao.add(curso)

  def incluir_questao(self, questao):
    curso = self.busca_curso_escolhido()
    curso._Curso__avaliacao.append(questao)
    self.__dao.update()
  
  def alterar_questao(self, numero_questao, questao):
    curso = self.busca_curso_escolhido()
    curso._Curso__avaliacao[numero_questao] = questao
    self.__dao.update()

  def remover_questao(self, numero_questao):
    curso = self.busca_curso_escolhido()
    curso._Curso__avaliacao.pop(numero_questao)
    self.__dao.update()
    
  def abre_aulas(self):
    self.__controlador_sistema.controlador_aula.listar_aulas()
    self.__controlador_sistema.abre_aulas()

  def abre_avaliacoes(self):
    self.__controlador_sistema.inclui_questao()

  def retornar(self):
    self.__tela_curso.close()
    self.__controlador_sistema.abre_tela()
   
  def adicionar_aula(self, aula):
    curso = self.busca_curso_escolhido()
    curso._Curso__lista_aulas.append(aula)
    self.__dao.update()
  
  def alterar_aula(self, numero_aula, aula):
    curso = self.busca_curso_escolhido()
    curso._Curso__lista_aulas[numero_aula] = aula
    self.__dao.update()

  def remover_aula(self, numero_aula):
    curso = self.busca_curso_escolhido()
    curso._Curso__lista_aulas.pop(numero_aula)
    self.__dao.update()

  def incluir_curso(self, dados_curso):
    codigo = self.get_next_key()
    curso = Curso(codigo, dados_curso["nome_curso"], dados_curso["descricao"], 
                    dados_curso["horas"])
    
    self.__dao.add(curso)

  def excluir_curso(self, curso):
    self.__dao.remove(curso.codigo)
    self.__controlador_sistema.controlador_progresso.remove_progresso_por_curso_cod(curso.codigo)
    self.__tela_curso.show_message('Sucesso', 'Curso Removido')

  def alterar_curso(self, curso, novos_dados):
    try:
      curso.nome_do_curso = novos_dados['nome_curso']
      curso.descricao = novos_dados['descricao']
      curso.quantidade_horas = novos_dados['horas']
      return True

    except:
      return False

  def alterar_curso_info(self, dados_antigos, curso):
    self.cadastrar_curso(dados_antigos, curso)
    self.__dao.update()
    self.__tela_curso.show_message('Sucesso', "Curso Alterado")

  def cadastrar_curso(self, curso = None, dados = None):
    # Tambem serve para alterar um curso existente
    self.__tela_curso.close()

    while True:

      if dados: # caso de alteracao
        button, values = self.__tela_curso.open_opcao(4, dados)

      else:  # caso de cadastro
        button, values = self.__tela_curso.open_opcao(3)

      if button == 1:
        self.__tela_curso.close_opcao()

        if (values["nome_curso"] != None and values["nome_curso"] != '') and (values["descricao"] != None and values["descricao"] != '') \
            and (values["horas"] != None and values["horas"] != ''):

          erro = False

          try:
            int(values["horas"])
          
          except ValueError:
            erro = True
            # Colocar Exception aqui!!
            self.__tela_curso.show_message("Erro", "Horas deve ser um valor inteiro")

          if not erro:
            # Em caso de cadastro (dados antigos is null)
            if not dados:
              self.incluir_curso(values)
            # Em caso de alteracao
            else:
              self.alterar_curso(curso, values)

            return True

        else:
          self.__tela_curso.show_message("Erro", "Preencha todas as caixas")
          self.__tela_curso.close_opcao()

      else:
        self.__tela_curso.close_opcao()
        return False

  def curso_to_json(self, curso):
    infos_curso = {}
    infos_curso["nome_curso"] = curso.nome_do_curso
    infos_curso["descricao"] = curso.descricao
    infos_curso["horas"] = curso.quantidade_horas

    return infos_curso

  def detalhes_curso(self, nome_curso):
    adm = self.__controlador_sistema.usuario_logado.adm
    self.__tela_curso.close()
    curso = self.pega_curso_por_nome(nome_curso)
    infos_curso = self.curso_to_json(curso)
    
    while True:
      button, values = self.__tela_curso.open_opcao(2, infos_curso, adm)

      if button != 0:
        self.__curso_escolhido = curso
        self.__tela_curso.close_opcao()

        if button == 1:
          self.abre_aulas()
          return True

        elif button == 2:
          self.abre_avaliacoes()
          return True

        elif button == 3:
          self.alterar_curso_info(curso, infos_curso)
          return True
        
        elif button == 4:
          self.excluir_curso(curso)
          return True

      self.__tela_curso.close_opcao()
      return False

  def listar_nome_cursos(self):
    self.__tela_curso.close()
    lista_nomes_cursos = []
    for curso in self.lista_cursos:
      lista_nomes_cursos.append(curso.nome_do_curso)
    
    while True:
      button, values = self.__tela_curso.open_opcao(1, lista_nomes_cursos)
      
      if button == 1:
        if len(values["nome_curso"]) > 0:
          self.__tela_curso.close_opcao()
          self.detalhes_curso(values["nome_curso"][0])
          return True
                  
        else:
          self.__tela_curso.show_message("Erro", "Selecione um curso")
          self.__tela_curso.close_opcao()

      else:
        self.__tela_curso.close_opcao()
        return False

  def abre_tela(self):
    adm = self.__controlador_sistema.usuario_logado.adm
    lista_opcoes = {1: self.listar_nome_cursos, 2: self.cadastrar_curso, 0: self.retornar}

    while True:
      lista_opcoes[self.__tela_curso.open(adm)]()
