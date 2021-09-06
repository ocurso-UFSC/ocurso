class TelaSistema:
    def tela_opcoes(self):
        print("-------- oCurso ---------")
        print("Escolha sua opcao")
        print("1 - Usuario")
        print("2 - Questao")
        print("3 - Cursos")
        print("4 - Progresso")
        print("9 - AUTOMATICO")
        print("0 - Sair do sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_mensagem(self, mensagem):
        print(mensagem)