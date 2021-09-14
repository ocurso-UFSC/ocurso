import PySimpleGUI as sg
class TelaSistema():
    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkBlue')
        botoes = [[sg.Button('Usuário', size=(20,2), key=1, button_color='#7B68EE')],
                  [sg.Button('Cursos', size=(20,2), key=2)],
                  [sg.Button('Progresso', size=(20,2), key=3)],
                  [sg.Button('AUTOMATICO', size=(20,2), key=9)],
                  [sg.Button('Sair do sistema', size=(20,2), key=0)]]

        layout = [[sg.Text('oCurso', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(botoes, vertical_alignment='center', justification='center', k='-C-')]]
        
        janela = sg.Window('oCurso').Layout(layout)
        button, values = janela.read()
        return button

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
