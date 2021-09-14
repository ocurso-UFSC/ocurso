import PySimpleGUI as sg
class TelaQuestao:
    def nome_curso(self):
        curso_selecionado = str(input('Qual curso? '))
        return curso_selecionado

    def tela_opcoes(self):
        adm = True
        sg.ChangeLookAndFeel('DarkBlue')
        botoes = [[sg.Button('Avaliações', size=(20,2), key=1, button_color='#7B68EE')],
                  [sg.Button('Adicionar questão', size=(20,2), key=2)],
                  [sg.Button('Alterar questão', size=(20,2), key=3)],
                  [sg.Button('Remover questão', size=(20,2), key=3)],
                  [sg.Button('Minhas notas', size=(20,2), key=9)],
                  [sg.Button('<-', size=(20,2), key=0)]]

        layout = [[sg.Text('oCurso', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]]
        
        janela = sg.Window('oCurso').Layout(layout)
        button, values = janela.read()
        return button

        # print ('---------- ESCOLHA A OPÇÃO ----------\n')
        # print ('Opção 1 - Mostrar avaliação final')
        # if adm:
        #     print ('Opção 2 - Adicionar questão')
        #     print ('Opção 3 - Alterar questão')
        #     print ('Opção 4 - Remover questão')
        # print ('Opção 9 - Mostrar minha nota')
        # print ('Opção 0 - Retornar')

        # opcao = int(input('\nEscolha uma das opções: '))
        # return opcao
    
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