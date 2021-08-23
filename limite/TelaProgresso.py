class TelaProgresso():
  def tela_opcoes(self):
    entrada = int(input(
'''
---------- oCurso  ------------
Escolha uma das opções a seguir
1 - Assistir
2 - Meu Relatório
3 - Todos Relatórios
0 - Voltar
Digite a opção: '''))

    return entrada
  
  def mostra_mensagem(self, msg):
    print(msg)