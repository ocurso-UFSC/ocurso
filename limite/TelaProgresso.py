class TelaProgresso():
  def tela_opcoes(self):
    entrada = int(input(
'''
---------- oCurso  ------------
Escolha uma das opções a seguir
1 - Me cadastrar no curso
2 - Meu Relatório
3 - Todos Relatórios
4 - Emitir meu certificado
0 - Voltar
Digite a opção: '''))

    return entrada
  
  def mostra_mensagem(self, msg):
    print(msg)
  
  def pega_entrada(self, msg):
    entrada = input(msg)
    return entrada