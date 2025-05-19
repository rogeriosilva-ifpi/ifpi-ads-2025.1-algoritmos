# letra a)

def funcao_numero_int():
    numero_int = int(input('Digite um número inteiro: '))
    print(numero_int)
    while numero_int % 1 == 0:
        numero_int = int(input('Digite outro número inteiro: '))
        print(numero_int)
        
programa_numero_int = funcao_numero_int()


# Letra b)
def int_positivo():
    numero_int = int(input('Digite um número inteiro: '))
    print(numero_int)
    while True:
        if numero_int % 1 == 0 and numero_int > 0:
            numero_int = int(input('Digite outro número inteiro: '))
            print(numero_int)
            
        else:
            print('esse número não é positivo')
            numero_int = int(input('Digite outro número: '))

programa_inteiro_postivo = int_positivo()

# Letra C)
def int_maior_q_x():
    numero_x = int(input('atribua um valor a X: '))
    numero_int_maior_q_x = int(input('Digite um número inteiro maior que X: '))
    while True:
        print(f'valor atribuido a X: {numero_x}')
        if numero_int_maior_q_x % 1 == 0 and numero_int_maior_q_x >= numero_x:
            numero_int_maior_q_x = int(input('Digite outro número inteiro maior que X: '))
            print(numero_int_maior_q_x)
            
        else:
            print(f'{numero_int_maior_q_x} não é maior que {numero_x}')
            numero_int_maior_q_x = int(input('Digite outro número: '))

programa_int_maior_q_x = int_maior_q_x()

# letra D)
def int_max_x():
    numero_x = int(input('atribua um valor a X: '))
    numero_int_max_x = int(input('Digite um número inteiro menor que X: '))
    while True:
        print(f'valor atribuido a X: {numero_x}')
        if numero_int_max_x % 1 == 0 and numero_int_max_x <= numero_x:
            numero_int_max_x = int(input('Digite outro número inteiro menor que X: '))
            print(numero_int_max_x)
            
        else:
            print(f'{numero_int_max_x} é maior que {numero_x}')
            numero_int_max_x = int(input('Digite outro número: '))

programa_int_max_x = int_max_x()

# Letra e)
def int_faixa_xy():
    numero_x = int(input('atribua um valor mínimo a X: '))
    numero_y = int(input('atribua um valor máximo a Y: '))
    numero_faixa_xy = int(input('Digite que esteja na faixa X e Y: '))
    while True:
        print(f'Faixa definida ({numero_x} a {numero_y})')
        if numero_faixa_xy % 1 == 0 and numero_x <= numero_faixa_xy <= numero_y:
            numero_faixa_xy = int(input('Digite outro número inteiro no intervalo X - Y: '))
            print(numero_faixa_xy)
            
        else:
            print(f'{numero_faixa_xy} está fora de faixa [{numero_x} - {numero_y}]')
            numero_faixa_xy = int(input('Digite outro número: '))

programa_faixa_xy = int_faixa_xy()