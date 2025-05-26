import os
# Nomear corretamente as questões de acordo com indicado.


def receber_numero_inteiro():
    # faltou retorno número
    # E tbm um label, text a ser exibido
    try:
        numero = int(input('Digite um número inteiro: '))
    except ValueError:
        print('O valor digitado deve ser um número inteiro, tente novamente')
        return receber_numero_inteiro()
    except:
        print('Erro inesperado')

    clear_screen()


def receber_numero_inteiro_positivo():
    # faltou returnar o número
    # faltou reusar a funcao base
    try:
        numero = int(input('Digite um número inteiro positivo: '))
        if numero < 0:
            print('O número deve ser maior que 0')
            return receber_numero_inteiro_positivo()
    except ValueError:
        print('O valor digitado deve ser um número inteiro, tente novamente')
        return receber_numero_inteiro_positivo()
    except:
        print('Erro inesperado')
    
    clear_screen()


def receber_numero_inteiro_limitado_min():

    try:
        limite_inferior = int(input('Digite um valor mínimo: '))
        numero = int(input('Digite um número inteiro: '))
        if numero < limite_inferior:
            print(f'O número deve ser maior ou igual a {limite_inferior}')
            return receber_numero_inteiro_limitado_min()
    except ValueError:
        print('O valor digitado deve ser um número inteiro, tente novamente')
        return receber_numero_inteiro_limitado_min()
    except:
        print('Erro inesperado')

    clear_screen()


def receber_numero_inteiro_limitado_max():
    try:
        limite_superior = int(input('Digite um valor máximo: '))
        numero = int(input('Digite um número inteiro: '))
        if numero > limite_superior:
            print(f'O número deve ser menor ou igual a {limite_superior}')
            return receber_numero_inteiro_limitado_max()
    except ValueError:
        print('O valor digitado deve ser um número inteiro, tente novamente')
        return receber_numero_inteiro_limitado_max()
    except:
        print('Erro inesperado')

        clear_screen()


def receber_numero_inteiro_limitado_min_max():
    try:
        limite_inferior = int(input('Digite um valor mínimo: '))
        limite_superior = int(input('Digite um valor máximo: '))
        numero = int(input('Digite um número inteiro: '))
        if numero > limite_superior or numero < limite_inferior:
            print(f'O número deve ser maior ou igual a {limite_inferior} e menor ou igual a {limite_superior}')
            return receber_numero_inteiro_limitado_min_max()
    except ValueError:
        print('O valor digitado deve ser um número inteiro, tente novamente')
        return receber_numero_inteiro_limitado_min_max()
    except:
        print('Erro inesperado')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostra_menu():
    menu = '''
    1 - Receber número inteiro
    2 - Receber número inteiro positivo
    3 - Receber número inteiro com valor mín
    4 - Receber número inteiro com valor máx
    5 - Receber número inteiro com valor mín e valor máx
    '''
    print(f'{menu}')
    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        receber_numero_inteiro()
    elif escolha == 2:
        receber_numero_inteiro_positivo()
    elif escolha == 3:
        receber_numero_inteiro_limitado_min()
    elif escolha == 4:
        receber_numero_inteiro_limitado_max()
    elif escolha == 5:
        receber_numero_inteiro_limitado_min_max()
    else:
        print('Escolha inválida')


mostra_menu()