class TelaProgresso():
  def tela_opcoes(self):
    entrada = int(input(
'''
---------- oCurso  ------------
Escolha uma das opções a seguir
1 - Meu Relatório
2 - Todos Relatórios
3 - Emitir meu certificado
0 - Voltar
Digite a opção: '''))

    return entrada
  
  def mostra_mensagem(self, msg):
    print(msg)