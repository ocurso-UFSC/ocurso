class TelaAula:
    def nome_curso(self):
        curso_selecionado = str(input('Qual curso? '))
        return curso_selecionado

    def continuar_aula(self):
        continuar = str(input('Deseja continuar? [ S | N ] ')).upper()
        return continuar
    
    def tela_opcoes(self):
        adm = True

        print ('---------- AULAS ----------\n')
        print ('Opção 1 - Ver aulas')
        if adm:
            print ('Opção 2 - Adicionar aula')
            print ('Opção 3 - Alterar aula')
            print ('Opção 4 - Remover aula')
        print ('Opção 5 - Listar aulas')
        print ('Opção 0 - Retornar')

        opcao = int(input('\nEscolha uma das opções: '))
        return opcao
    
    def lista_aulas(self, numero_aula, descricao):
        print (f'Aula {numero_aula} - {descricao}')

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
