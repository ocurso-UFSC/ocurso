import PySimpleGUI as sg

class TelaSistema():
    def __init__(self):
        self.__window = None

    def init_components(self):
        sg.ChangeLookAndFeel('DarkBlue')
        botoes = [[sg.Button('Usuário', size=(20,2), key=1, button_color='#7B68EE')],
                  [sg.Button('Cursos', size=(20,2), key=2, button_color='#7B68EE')],
                  [sg.Button('Progresso', size=(20,2), key=3, button_color='#7B68EE')],
                  [sg.Button('AUTOMATICO', size=(20,2), key=9, button_color='#7B68EE')],
                  [sg.Button('Deslogar', size=(20,2), key=0)]]

        layout = [[sg.Text('oCurso', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]]

        self.__window = sg.Window("oCurso", default_element_size=(40, 1)).Layout(layout)
    
    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button

    def close(self):
        if self.__window != None:
            self.__window.Close()
            self.__window = None

    def mostra_mensagem(self, mensagem):
        sg.Popup(mensagem)