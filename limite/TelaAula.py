class TelaAula:
    def tela_opcoes(self):
        opcao = int(input(
        '''
Você deseja acessar a aula de qual curso?

Opção 1 - Python

Escolha a opção: '''))

        return opcao

    def mostra_aulas(self, chave_aula):
        print (chave_aula)

    def mostra_mensagem(self, msg):
        print(msg)