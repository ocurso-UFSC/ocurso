class TelaQuestao:
    def tela_opcoes(self):
        adm = True

        print ('---------- ESCOLHA A OPÇÃO ----------\n')
        print ('Opção 1 - Mostrar avaliação final')
        if adm:
            print ('Opção 2 - Adicionar questão')
            print ('Opção 3 - Alterar questão')
            print ('Opção 4 - Remover questão')
        print ('Opção 9 - Mostrar minha nota')
        print ('Opção 0 - Retornar')

        opcao = int(input('\nEscolha uma das opções: '))
        return opcao
    
    def quantidade(self, msg):
        quantidade = int(input(msg))
        return quantidade
    
    def alternativa(self, msg):
        descricao_alternativa = str(input(msg))
        return descricao_alternativa

    def infos_questao(self):
        descricao_questao = str(input('Escreva a sua descrição: '))
        alternativa_correta = str(input('Informe quais das alternativas da questão é a correta: '))

        return {
            'descricao_questao':descricao_questao,
            # 'lista_alternativas':lista_alternativas,
            'alternativa_correta':alternativa_correta,
        }

    def alterando_questao(self):
        numero_questao = int(input('Informe o número da questão: '))
        return numero_questao

    def mostra_descricao(self, numero_questao, descricao):
        print(f'{numero_questao} - {descricao}')

    def mostra_pergunta(self, index, alternativa):
        print (f'   {index}) {alternativa}')

    def pega_resposta(self):
        resposta_usuario = str(input('\nSua resposta: '))
        return resposta_usuario

    def mostra_resposta(self, numero_questao, resposta_correta):
        print (f'Resposta da questão {numero_questao+1}: {resposta_correta.upper()}')

    def mostra_mensagem(self, msg):
        print(msg)