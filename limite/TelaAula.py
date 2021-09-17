import PySimpleGUI as sg
class TelaAula:
    def __init__(self):
        self.__window = None
        self.__window2 = None
        self.__window3 = None
        self.__aulas = []
        self.init_components()

    def init_components(self):
        aulas = []
        for aula in self.__aulas:
            aulas.append([sg.Text(f'{aula[0]} - {aula[1]}')])
        sg.ChangeLookAndFeel('DarkBlue')
        ver_aulas = [[sg.Button('Ver aulas', size=(20,2), key=1, button_color='#7B68EE')]]

        # if adm
        botoes = [[sg.Button('+', size=(5,2), key=2, button_color='#7B68EE'),
                  sg.Button('Alterar', size=(5,2), key=3, button_color='#7B68EE'),
                  sg.Button('X', size=(5,2), key=4, button_color='#7B68EE')]]

        layout = [[sg.Text('Aulas', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(aulas, vertical_alignment='center', justification='center')],
                  [sg.Column(ver_aulas, vertical_alignment='center', justification='center')],
                  [sg.Column(botoes, vertical_alignment='center', justification='center')],
                  [sg.Button('<-', size=(2,1), key=0)]]

        self.__window = sg.Window("Aulas", layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        print(button, values)
        return button

    def close(self):
        self.__window.Close()
    
    def close_mexe_na_aula(self):
        self.__window2.Close()
    
    def close_pega_dados_aula(self):
        self.__window3.Close()

    def continuar_aula(self):
        continuar = str(input('Deseja continuar? [ S | N ] ')).upper()
        return continuar

    def lista_aulas(self, index_aula, descricao_aula):
        self.__aulas.append([index_aula, descricao_aula])
    
    def limpar_lista_aulas(self):
        self.__aulas = []

    def mostra_aulas(self, numero_aula, descricao, link):
        print ('\n' + '-'*50)
        print (f'Aula {numero_aula} - {descricao}\
                \n   {link}')

    def pega_dados_aula(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [[sg.InputText('Descrição da Aula:', size=(20,2), key="descricao_aula")],
                  [sg.InputText('Link da Aula:', size=(20,2), key="link_aula")],
                  [sg.Button('Enviar', size=(10,1), button_color='#7B68EE')]]
                
        self.__window3 = sg.Window("Aula", layout)

        # descricao_aula = str(input('Escreva aqui a descrição da aula: '))
        # link_aula = str(input('Link da aula: '))
    
    def open_pega_dados_aula(self):
        self.pega_dados_aula()
        button, values = self.__window3.Read()
        print (values)
        return values
            
    def mexe_na_aula(self, mensagem):
        aulas = []
        for aula in self.__aulas:
            aulas.append([sg.Radio('', 'index_aula', key=aula[0]), sg.Text(f'{aula[0]} - {aula[1]}')])
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [[sg.Text(f'{mensagem}', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(aulas, vertical_alignment='center', justification='center')],
                  [sg.Button('Selecionar aula', size=(10,1), button_color='#7B68EE')]]

        self.__window2 = sg.Window("Editar aula", default_element_size=(30, 1)).Layout(layout)
    
    def open_mexe_na_aula(self, mensagem):
        self.mexe_na_aula(mensagem)
        button, values = self.__window2.Read()
        valor_aula = []
        for key in values:
            if values[key] == True:
                valor_aula.append(key)

        return valor_aula[0] - 1

    def mostra_mensagem(self, msg):
        print(msg)
