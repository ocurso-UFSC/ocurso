import PySimpleGUI as sg

class TelaSistema():
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkBlue')
        botoes = [[sg.Button('Usuário', size=(20,2), key=1, button_color='#7B68EE')],
                  [sg.Button('Cursos', size=(20,2), key=2, button_color='#7B68EE')],
                  [sg.Button('Progresso', size=(20,2), key=3, button_color='#7B68EE')],
                  [sg.Button('AUTOMATICO', size=(20,2), key=9, button_color='#7B68EE')],
                  [sg.Button('Sair do sistema', size=(20,2), key=0)]]

        layout = [[sg.Text('oCurso', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]]

        self.__window = sg.Window("Titulo", default_element_size=(40, 1)).Layout(layout)
    
    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def mostra_mensagem(self, mensagem):
        sg.Popup(mensagem)



        # print("-------- oCurso ---------")
        # print("Escolha sua opcao")
        # print("1 - Usuario")
        # print("2 - Cursos")
        # print("3 - Progresso")
        # print("9 - AUTOMATICO")
        # print("0 - Sair do sistema")
        # opcao = int(input("Escolha a opcao: "))
        # return opcao
