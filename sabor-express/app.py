import os

restaurantes = [{'nome':'Zoiudos', 'categoria':'Brasileira','ativo':False},
                {'nome':'Gorditus', 'categoria':'Francesa', 'ativo':True},
                {'nome':'Mercenarius','categoria':'Mexicana','ativo':False}]


def exibir_nome():
    '''Mostra o titulo'''
    print("""

░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 █▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 █▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ▀▀▀ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀ \n""")
    

def exibir_opcoes():
    '''Da as opções pro usuario'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair \n')


def voltar_ao_menu():
    '''Volta do começo'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    '''Os titulos para cada opção'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def alterar_estado_restaurante():
    '''Deixa o restaurante ativado ou desativado'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso!'
                if restaurante['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            )
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_ao_menu()



def cadastrar_novo_restaurante():
    '''Adiciona na lista de restaurantes 
    
    inputs:
    - nome do restaurante
    - categoria

    outputs:
    - Adiciona um novo restaurante na lista
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = str(input('Nome do restaurante que deseja cadastrar: '))
    categoria = str(input(f'Digite o nome da categoria do restaurante {nome_restaurante}: '))
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso! \n')
    voltar_ao_menu()

def listar_restaurante():
    '''Mostra a listagem de restaurantes cadastrados'''
    
    exibir_subtitulo('Lista de restaurantes!')

    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' 
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()

def finalizar_app():
    '''vai pra uma pagina que so diz que encerrou'''
    exibir_subtitulo('Encerrando app!')
    
def opcao_invalida():
    '''se o usuario não escolher nenhuma opção valida'''
    print('Opção invalida! \n')
    voltar_ao_menu() 


def escolha():
    '''faz oque o usuario escolher com as funções'''
    try:
        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            cadastrar_novo_restaurante()
        elif escolha == 2:
            listar_restaurante()
        elif escolha == 3:
            alterar_estado_restaurante()
        elif escolha == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    '''Oque roda tudo'''
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolha()

if __name__ == '__main__':
    main()