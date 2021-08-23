from entidade.aula import Aula

class TelaAula:
    def tela_opcoes(self):
        print('O que você deseja fazer?')
        print('Opção 1 - Mostrar conteúdos do curso')

        #if usuario é adm:
        print('Opção 2 - Adicionar conteúdo')
        print('Opção 3 - Editar conteúdo')
        print('Opção 4 - Remover conteúdo')
        #fim do if usuario é adm

        print('Opção 0 - Retornar')

        opcao = int(input('Escolha a opção: '))
        return opcao

    def mostra_aulas(self, descricao, link):
        print (f'\n   {descricao}\n   {link}')
        print ('-'*50)

    def mostra_mensagem(self, msg):
        print(msg)
