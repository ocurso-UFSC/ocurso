class TelaAula:
    def nome_curso(self):
        curso_selecionado = str(input('De qual curso? '))
        return curso_selecionado
    
    def tela_opcoes(self):
        adm = True

        print ('---------- AULAS ----------\n')
        print ('Opção 1 - Ver aulas')
        if adm:
            print ('Opção 2 - Adicionar aula')
            print ('Opção 3 - Alterar aula')
            print ('Opção 4 - Remover aula')
        print ('Opção 0 - Retornar')

        opcao = int(input('\nEscolha uma das opções: '))
        return opcao

    def mostra_aulas(self, descricao, link):
        print (f'\n   {descricao}\n   {link}')
        print ('-'*50)
    
    def pega_dados_aula(self):
        descricao_aula = str(input('Escreva aqui a descrição da aula: '))
        link_aula = str(input('Link da aula: '))
        return {'descricao_aula':descricao_aula,
                'link_aula':link_aula}

    def mostra_mensagem(self, msg):
        print(msg)
