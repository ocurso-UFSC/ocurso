class TelaQuestao:
    def tela_opcoes(self):
        adm = True

        print ('---------- ESCOLHA A OPÇÃO ----------\n')
        print ('Opção 1 - Mostrar avaliação final')
        if adm:
            print ('Opção 2 - Adicionar questão')
            print ('Opção 3 - Alterar questão')
            print ('Opção 4 - Remover questão')
        print ('Opção 9 - Mostrar respostas')
        print ('Opção 0 - Retornar')

        opcao = int(input('\nEscolha uma das opções: '))
        return opcao

    def infos_questao(self):
        descricao_questao = str(input('Descrição da questão: '))

        alternativas = {}

        quantidade_alternativas = int(input('Quantas alternativas você deseja adicionar na questão? '))
        for c in range (quantidade_alternativas):
            index = str(input(f'Digite o index da {c+1} alternativa: ')).lower()
            resposta = str(input(f'Digite a resposta da {c+1} alternativa: '))
            print ('')
            alternativas[index] = resposta
        alternativa_correta = str(input('Informe quais das alternativas da questão é a correta: '))

        return {
            'descricao_questao':descricao_questao,
            'alternativas':alternativas,
            'alternativa_correta':alternativa_correta,
        }

    def alterando_questao(self):
        numero_questao = int(input('Informe o número da questão: '))
        return numero_questao

    def mostra_descricao(self, numero_questao, descricao):
        print(f'{numero_questao} - {descricao}')

    def mostra_pergunta(self, alternativa, index):
        print (f'   {index}) {alternativa}')

    def mostra_resposta(self, numero_questao, resposta_correta):
        print (f'Resposta da questão {numero_questao+1}: {resposta_correta.upper()}')

    def mostra_mensagem(self, msg):
        print(msg)