class TelaSistema:
    def tela_opcoes(self):
        print("-------- oCurso ---------")
        print("Escolha sua opcao")
        print("1 - Usuario")
        print("2 - Questao")
        print("3 - Cursos")
        print("0 - Deslogar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_mensagem(self, mensagem):
        print(mensagem)