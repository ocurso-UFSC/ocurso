import PySimpleGUI as sg
class TelaAula:
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkBlue')
        botoes = [[sg.Button('Ver aulas', size=(20,2), key=1, button_color='#7B68EE')],
                  [sg.Button('Adicionar aula', size=(20,2), key=2, button_color='#7B68EE')],
                  [sg.Button('Alterar aula', size=(20,2), key=3, button_color='#7B68EE')],
                  [sg.Button('Remover aula', size=(20,2), key=4, button_color='#7B68EE')],
                  [sg.Button('Listar aulas', size=(20,2), key=5, button_color='#7B68EE')],
                  [sg.Button('<-', size=(20,2), key=0)]]

        layout = [[sg.Text('Aulas', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(botoes, vertical_alignment='center', justification='center')]]

        self.__window = sg.Window("Aulas", default_element_size=(40, 1)).Layout(layout)
    
    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()


    # def tela_opcoes(self):
    #     adm = True

    #     print ('---------- AULAS ----------\n')
    #     print ('Opção 1 - Ver aulas')
    #     if adm:
    #         print ('Opção 2 - Adicionar aula')
    #         print ('Opção 3 - Alterar aula')
    #         print ('Opção 4 - Remover aula')
    #     print ('Opção 5 - Listar aulas')
    #     print ('Opção 0 - Retornar')

    #     opcao = int(input('\nEscolha uma das opções: '))
    #     return opcao
    
    def nome_curso(self):
        curso_selecionado = str(input('Qual curso? '))
        return curso_selecionado

    def continuar_aula(self):
        continuar = str(input('Deseja continuar? [ S | N ] ')).upper()
        return continuar

    def lista_aulas(self, lista_de_aulas):
        aulas = lista_de_aulas
        ver_aulas = [[sg.Button('Ver aulas', size=(20,2), key=1, button_color='#7B68EE')]]
        botoes = [[sg.Button('Adicionar \naula', size=(5,2), key=2, button_color='#7B68EE'),
                  sg.Button('Alterar \naula', size=(5,2), key=3, button_color='#7B68EE'),
                  sg.Button('Remover \naula', size=(5,2), key=4, button_color='#7B68EE')]]
        layout = [[sg.Text('Aulas', size=(15, 2), font=('Helvetica', 20), justification=('center'))],
                  [sg.Column(aulas, vertical_alignment='center', justification='center')],
                  [sg.Column(ver_aulas, vertical_alignment='center', justification='center')],
                  [sg.Column(botoes, vertical_alignment='center', justification='center')],
                  [sg.Button('<-', size=(2,1), key=0)]]
        self.__window = sg.Window("Aulas", default_element_size=(40, 1)).Layout(layout)
        button, values = self.__window.Read()
        return button



    def mostra_aulas(self, numero_aula, descricao, link):
        print ('\n' + '-'*50)
        print (f'Aula {numero_aula} - {descricao}\
                \n   {link}')
    
    def pega_dados_aula(self):
        descricao_aula = str(input('Escreva aqui a descrição da aula: '))
        link_aula = str(input('Link da aula: '))
        return {'descricao_aula':descricao_aula,
                'link_aula':link_aula}
            
    def mexe_na_aula(self, mensagem):
        numero_aula = int(input(mensagem)) - 1
        return numero_aula

    def mostra_mensagem(self, msg):
        print(msg)
