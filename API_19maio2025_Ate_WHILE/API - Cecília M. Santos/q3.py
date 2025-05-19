import os


def receber_numero_decimal():
    try:
        numero = float(input('Digite um número decimal: '))
    except ValueError:
        print('O valor digitado deve ser um número decimal, tente novamente')
        return receber_numero_decimal()
    except:
        print('Erro inesperado')

    clear_screen()


def receber_numero_decimal_positivo():
    try:
        numero = float(input('Digite um número decimal positivo: '))
        if numero < 0:
            print('O número deve ser maior que 0')
            return receber_numero_decimal_positivo()
    except ValueError:
        print('O valor digitado deve ser um número decimal, tente novamente')
        return receber_numero_decimal_positivo()
    except:
        print('Erro inesperado')
    
    clear_screen()


def receber_numero_decimal_limitado_min():
    try:
        limite_inferior = float(input('Digite um valor mínimo: '))
        numero = float(input('Digite um número decimal: '))
        if numero < limite_inferior:
            print(f'O número deve ser maior ou igual a {limite_inferior}')
            return receber_numero_decimal_limitado_min()
    except ValueError:
        print('O valor digitado deve ser um número decimal, tente novamente')
        return receber_numero_decimal_limitado_min()
    except:
        print('Erro inesperado')

    clear_screen()


def receber_numero_decimal_limitado_max():
    try:
        limite_superior = float(input('Digite um valor máximo: '))
        numero = float(input('Digite um número decimal: '))
        if numero > limite_superior:
            print(f'O número deve ser menor ou igual a {limite_superior}')
            return receber_numero_decimal_limitado_max()
    except ValueError:
        print('O valor digitado deve ser um número decimal, tente novamente')
        return receber_numero_decimal_limitado_max()
    except:
        print('Erro inesperado')

        clear_screen()


def receber_numero_decimal_limitado_min_max():
    try:
        limite_inferior = float(input('Digite um valor mínimo: '))
        limite_superior = float(input('Digite um valor máximo: '))
        numero = float(input('Digite um número decimal: '))
        if numero > limite_superior or numero < limite_inferior:
            print(f'O número deve ser maior ou igual a {limite_inferior} e menor ou igual a {limite_superior}')
            return receber_numero_decimal_limitado_min_max()
    except ValueError:
        print('O valor digitado deve ser um número decimal, tente novamente')
        return receber_numero_decimal_limitado_min_max()
    except:
        print('Erro inesperado')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostra_menu():
    menu = '''
    1 - Receber número decimal
    2 - Receber número decimal positivo
    3 - Receber número decimal com valor mín
    4 - Receber número decimal com valor máx
    5 - Receber número decimal com valor mín e valor máx
    '''
    print(f'{menu}')
    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        receber_numero_decimal()
    elif escolha == 2:
        receber_numero_decimal_positivo()
    elif escolha == 3:
        receber_numero_decimal_limitado_min()
    elif escolha == 4:
        receber_numero_decimal_limitado_max()
    elif escolha == 5:
        receber_numero_decimal_limitado_min_max()
    else:
        print('Escolha inválida')


mostra_menu()