class TelaQuestao:
    def tela_opcoes(self):
        adm = False

        print ('---------- ESCOLHA A OPÇÃO ----------\n')
        print ('Opção 1 - Mostrar perguntas')
        if adm:
            print ('Opção 2 - Adicionar pergunta')
        print ('Opção 0 - Retornar')

        opcao = int(input('\nEscolha uma das opções: '))
        return opcao

    def infos_questao(self):
        print ('---------- ADICIONANDO QUESTAO ----------')
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

    def mostra_descricao(self, descricao):
        print(descricao)

    def mostra_pergunta(self, alternativa, index):
        print (f'   {index}) {alternativa}')