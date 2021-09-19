import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Open
class TelaAula:
    def __init__(self):
        self.__window = None
        self.__window2 = None
        self.__window3 = None
        self.__aulas = []

    #telas e microtelas
    def tela_aula(self, adm):
        aulas = []
        for aula in self.__aulas:
            aulas.append([sg.Text(f'{aula[0]} - {aula[1]}')])
        sg.ChangeLookAndFeel('DarkBlue')
        ver_aulas = [[sg.Button('Ver aulas', size=(20,2), key=1, button_color='#7B68EE')]]

        botoes = [[sg.Button('+', size=(5,2), key=2, button_color='#7B68EE'),
                  sg.Button('Alterar', size=(5,2), key=3, button_color='#7B68EE'),
                  sg.Button('X', size=(5,2), key=4, button_color='#7B68EE')]]
        
        if adm == True:
            layout = [[sg.Text('Aulas', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                    [sg.Column(aulas, vertical_alignment='center', justification='center')],
                    [sg.Column(ver_aulas, vertical_alignment='center', justification='center')],
                    [sg.Column(botoes, vertical_alignment='center', justification='center')],
                    [sg.Button('<-', size=(2,1), key=0)]]
        else:
            layout = [[sg.Text('Aulas', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                    [sg.Column(aulas, vertical_alignment='center', justification='center')],
                    [sg.Column(ver_aulas, vertical_alignment='center', justification='center')],
                    [sg.Button('<-', size=(2,1), key=0)]]


        self.__window = sg.Window("Aulas", layout)

    def lista_aulas(self, index_aula, descricao_aula):
        self.__aulas.append([index_aula, descricao_aula])
    
    def limpar_lista_aulas(self):
        self.__aulas = []

    def mostra_aulas(self, numero_aula, descricao, link):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [[sg.Text(f'{numero_aula} - {descricao}', font=('Helvetica', 20), justification=('center'))],
                  [sg.Text(f'Link da aula:\n   {link}', size=(15,2), justification=('center'))],
                  [sg.Button('Sair', size=(5,2), key='N', button_color='#7B68EE'),
                   sg.Button('->', size=(5,2), key='S', button_color='#7B68EE')]]
                
        self.__window3 = sg.Window(f'Aula {numero_aula}', layout)

    def pega_dados_aula(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [[sg.InputText('Descrição da Aula:', size=(20,2), key="descricao_aula")],
                  [sg.InputText('Link da Aula:', size=(20,2), key="link_aula")],
                  [sg.Button('Enviar', size=(10,1), button_color='#7B68EE')]]
                
        self.__window3 = sg.Window("Aula", layout)
            
    def mexe_na_aula(self, mensagem):
        aulas = []
        for aula in self.__aulas:
            aulas.append([sg.Radio('', 'index_aula', key=aula[0]), sg.Text(f'{aula[0]} - {aula[1]}')])
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [[sg.Text(f'{mensagem}', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(aulas, vertical_alignment='center', justification='center')],
                  [sg.Button('Selecionar aula', size=(10,1), button_color='#7B68EE')]]

        self.__window2 = sg.Window("Editar aula", default_element_size=(30, 1)).Layout(layout)

    def mostra_mensagem(self, titulo, mensagem):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [[sg.Text(f'{titulo}', font=('Helvetica', 20), justification=('center'))],
                  [sg.Text(f'{mensagem}', size=(30,3), justification=('center'))],
                  [sg.Button('OK', size=(5,2), button_color='#7B68EE')]]
                
        self.__window2 = sg.Window("Curso concluído", default_element_size=(30, 2)).Layout(layout)
    
    def pergunta (self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [[sg.Text(f'Aulas', font=('Helvetica', 20), justification=('center'))],
                  [sg.Text(f'Você já assistiu as aulas deste curso. \nDeseja assistir novamente?', size=(30,3), justification=('center'))],
                  [sg.Button('Sim', size=(5,2), key='yes', button_color='#7B68EE'),
                   sg.Button('Não', size=(5,2), key='no', button_color='#7B68EE')]]
        
        self.__window2 = sg.Window("Ver aulas", default_element_size=(30, 2)).Layout(layout)

    #Open's
    def open(self, adm):
        self.tela_aula(adm)
        button, values = self.__window.Read()
        return button

    def open_mostra_aulas(self, numero_aula, descricao, link):
        self.mostra_aulas(numero_aula, descricao, link)
        button, values = self.__window3.Read()
        return button

    def open_pega_dados_aula(self):
        self.pega_dados_aula()
        button, values = self.__window3.Read()
        return values

    def open_mexe_na_aula(self, mensagem):
        self.mexe_na_aula(mensagem)
        button, values = self.__window2.Read()
        valor_aula = []
        for key in values:
            if values[key] == True:
                valor_aula.append(key)

        return valor_aula[0] - 1

    def open_mensagem(self, titulo, mensagem):
        self.mostra_mensagem(titulo, mensagem)
        button, values = self.__window2.Read()
        return button

    def open_pergunta(self):
        self.pergunta()
        button, values = self.__window2.Read()
        return button

    #Close's
    def close(self):
        self.__window.Close()
    
    def close_mexe_na_aula(self):
        self.__window2.Close()
    
    def close_pega_dados_aula(self):
        self.__window3.Close()
