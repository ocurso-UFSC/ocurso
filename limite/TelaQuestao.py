import PySimpleGUI as sg
class TelaQuestao():
    def __init__(self):
        self.__window = None
        self.__window2 = None
        self.__window3 = None

    #telas e microtelas
    def tela_opcoes(self, adm=False):
        sg.ChangeLookAndFeel('DarkBlue')
        if adm == True:
            botoes = [[sg.Button('Avaliação', size=(20,2), key=1, button_color='#7B68EE')],
                      [sg.Button('Adicionar questão', size=(20,2), key=2)],
                      [sg.Button('Editar avaliação', size=(20,2), key=5)],
                      [sg.Button('Minha nota', size=(20,2), key=9)],
                      [sg.Button('<-', size=(20,2), key=0)]]
        else:
            botoes = [[sg.Button('Avaliação', size=(20,2), key=1, button_color='#7B68EE')],
                      [sg.Button('Minha nota', size=(20,2), key=9)],
                      [sg.Button('<-', size=(20,2), key=0)]]

        layout = [[sg.Text('oCurso', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(botoes, vertical_alignment='center', justification='center')]]
        
        self.__window = sg.Window('oCurso').Layout(layout)
    
    def quantidade(self, msg):
        quantidade = int(input(msg))
        return quantidade
    
    def alternativa(self, index):
        sg.ChangeLookAndFeel('DarkBlue')
        descricao_alternativa = [[sg.Text(f'Alternativa {index}', size=(30, 1), font=("Helvetica", 15))],
                                 [sg.InputText('', key="descricao_alternativa")]]

        layout = [[sg.Column(descricao_alternativa, vertical_alignment='center', justification='center')],
                  [sg.Button('->', size=(2,1), key=0)]]
        
        self.__window2 = sg.Window("Adicionando questão", default_element_size=(40, 3)).Layout(layout)

    def infos_questao(self):
        sg.ChangeLookAndFeel('DarkBlue')

        infos = [
        [sg.Text('Descrição da questão', size=(30, 1), font=("Helvetica", 15))],
            [sg.InputText('', key="descricao_questao")],
        [sg.Text('Quantidade de alternativas', size=(30, 1), font=("Helvetica", 15))],
            [sg.Spin(values=(2, 3, 4, 5, 6), size=(5, 5), initial_value=2, key="quantidade_alternativas")]]

        layout = [[sg.Column(infos, vertical_alignment='center', justification='center')],
                  [sg.Button('->', size=(2,1), key=0)]]
        
        self.__window3 = sg.Window("Adicionando questão", default_element_size=(40, 3)).Layout(layout)

    def alternativa_correta(self, alternativas):
        sg.ChangeLookAndFeel('DarkBlue')
        botoes = [[sg.Button("->", key=1)]]
        layout = [
            [sg.Text('Selecione a correta', size=(15, 1), font=("Helvetica", 12))],
            [sg.Listbox(values=alternativas, key="alternativa", size=(20, 10))],
            [sg.Column(botoes, justification='center')],
        ]

        self.__window2 = sg.Window("Avaliação", default_element_size=(100, 1)).Layout(layout)

    def mostra_pergunta(self, questao, alternativas):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [[sg.Text(f'{questao}', justification=('center'))],
                  [sg.Listbox(alternativas, key="questao", size=(20, 10))],
                  [sg.Button('->', size=(5,2), button_color='#7B68EE')]]

        self.__window2 = sg.Window("Avaliação").Layout(layout)

    def mostra_mensagem(self, titulo, mensagem):
        sg.ChangeLookAndFeel('DarkBlue')
        if float(mensagem) >= 7:
            layout = [[sg.Text(f'{titulo}', justification=('center'))],
                    [sg.Text(f'{mensagem}', font=('Helvetica', 20), text_color='#98FB98', justification=('center'))],
                    [sg.Text(f'Você está aprovado!', justification=('center'))],
                    [sg.Button('OK', size=(5,2), button_color='#7B68EE')]]
        else:
            layout = [[sg.Text(f'{titulo}', justification=('center'))],
                    [sg.Text(f'{mensagem}', font=('Helvetica', 20), text_color='#CD5C5C', justification=('center'))],
                    [sg.Button('OK', size=(5,2), button_color='#7B68EE')]]

        self.__window2 = sg.Window('oCurso').Layout(layout)

    def listar_questoes(self, lista_questoes):
        botoes = [[sg.Button("X", key=2), sg.Button("Editar", key=1), sg.Button("<-", key=0)]]
        layout = [
            [sg.Text('Questões da avaliação', size=(15, 1), font=("Helvetica", 15))],
            [sg.Listbox(values=lista_questoes, key="questao", size=(20, 10))],
            [sg.Column(botoes, justification='center')],
        ]

        self.__window2 = sg.Window("Avaliação", default_element_size=(100, 1)).Layout(layout)

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)

    #Open's:
    def open_window(self, adm):
        self.tela_opcoes(adm)
        button, values = self.__window.Read()
        return button

    def open_alternativa(self, index):
        self.alternativa(index)
        button, values = self.__window2.Read()
        return values['descricao_alternativa']

    def open_infos_questao(self):
        self.infos_questao()
        button, values = self.__window3.Read()
        return values

    def open_alternativa_correta(self, alternativas):
        self.alternativa_correta(alternativas)
        button, values = self.__window2.Read()
        return values['alternativa'][0][0]

    def open_mostra_pergunta(self, questao=None, alternativas=None):
        while True:
            self.mostra_pergunta(questao, alternativas)
            button, values = self.__window2.Read()
            try:
                resposta = values['questao'][0][0]
                break
            except:
                self.close_window2()
                self.show_message('Atenção!', 'Selecione uma alternativa.')
        return resposta

    def open_mostra_mensagem(self, titulo, mensagem):
        self.mostra_mensagem(titulo, mensagem)
        button, values = self.__window2.Read()
        return button

    def open_listar_questoes(self, lista_questoes):
        self.listar_questoes(lista_questoes)
        button, values = self.__window2.Read()
        return button, values

    #Close's:
    def close_window(self):
        self.__window.Close()
        self.__window = None

    def close_window2(self):
        if self.__window2 != None:
            self.__window2.Close()
        self.__window2 = None

    def close_window3(self):
        self.__window3.Close()
        self.__window3 = None
