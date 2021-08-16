class TelaAula:
    def tela_opcoes(self):
        opcao = int(input(
        '''
        Você deseja acessar a aula de qual curso?\n')
        Opção 1 - Python

        Escolha a opção: '''))

        return opcao

    def mostra_mensagem(self, msg):
        print(msg)