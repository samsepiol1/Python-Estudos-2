from algoritmo_do_cara import modo_crackudo,modo_maconheiro,pesquisa_avancada

def inicio():
    MENU = '''
        _____________________________________
        |                                   |
        |      1 - gerador simples          |
        |      2 - gerador crackudo         |
        |      3 - sair 
               4- pesquisa avançada
                                           |
        |___________________________________| '''

    print(MENU)
    modo=input('Digita o número:')
    if modo=='1':
        modo_maconheiro()
    elif modo=='2':
        modo_crackudo()
    elif modo=='3':
        exit
    elif modo=='4':
        pesquisa_avancada()
    else:
        print('Digita isso certo!')
inicio()