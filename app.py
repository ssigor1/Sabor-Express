import os

restaurantes = [{'nome':'Praça', 'categoria':'Japones', 'ativo': False},
                {'nome':'Pizza suprema', 'categoria': 'Italiana', 'ativo':True},
                {'nome':'Biroliro', 'categoria':'Frances', 'ativo': False}]

def exibir_nome_do_programa():
    '''Exibe o Título do programa 
    Output: print()    
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Exibe as opções disponíveis para a seleção
    Output: print()
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Puxa a função exibir_subtitulo para sinalizar que o app foi encerrado
    output: exibir_subtitulo'''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''faz com que o programa volte para a escolha de opções
    Input: 'digite qualquer tecla para voltar ao menu'
    output: volta ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Informa que o valor não coincide com as opções atuais
    output: imprime a frase(Opção invalida) e volta ao menu principal'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Limpa o terminal, cria um bloco de * com o subtitulo dentro dele
    input: linha
    output: adiciona o texto dentro de um bloco de (*) '''
    os.system('cls')
    linha = '*' *(len(texto)+4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - nome_do_restaurante
    - categoria

    output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''essa função é responsável por listar todos os restaurantes, categorias e status
    input: 
    - nome_restaurante
    - categoria
    - ativo
    
    output: recebe o nome e categoria do restaurante salvando na lista, caso a variavel *ativo* estiver com o valor true, mostrará (ativado) senão mostrará (desativado)'''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo ='Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''' essa função é responsável por alterar o Status do restaurante pesquisado
    input:
    - nome_restaurante
    - restaurante_encontrado
    - restaurante['ativo']
    - mensagem
    
    output: 
    - a função alterna entre ativo e inativo, caso o restaurante pesquisado não tenha sido encontrado com base na pesquisa, o terminal imprimirá (O restaurante não foi encontrado)'''
    exibir_subtitulo('Alternando estado do Restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsável por possibilitar dar a escolha ao usuário 
    input: 
    - opcao_escolhida
    
    output:
    - com base em sua escolha, o programa avançará para a opção escolhida, caso sua escolha não seja válida, mostrará a função de opção inválida'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''mostra o menu inicial
    output:
    - mostra o nome do programa, as opções e a função para o usuário escolher'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    '''Função feita para tornar o arquivo main()'''
    main()