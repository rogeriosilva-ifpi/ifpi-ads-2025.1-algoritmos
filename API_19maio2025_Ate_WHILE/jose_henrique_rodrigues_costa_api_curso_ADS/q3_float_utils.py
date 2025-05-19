# letra a)
def funcao_numero_float():
    numero_float = float(input('Digite um número decimal: '))
    print(numero_float)
        
        
programa_numero_float = funcao_numero_float()

# letra B)
def float_postivo():
    numero_float = float(input('Digite um número decimal: '))
    print(numero_float)
    while True:
        if numero_float > 0:
            numero_float = float(input('Digite outro número decimal: '))
            print(numero_float)
            
        else:
            print(f'{numero_float} não é positivo')
            numero_float = float(input('Digite outro número: '))
            
            
programa_float_positivo = float_postivo()


# Letra C)
def float_maior_q_x():
    numero_x = float(input('atribua um valor a X: '))
    numero_float_maior_q_x = float(input('Digite um número inteiro maior que X: '))
    while True:
        print(f'valor atribuido a X: {numero_x}')
        if numero_float_maior_q_x >= numero_x:
            numero_float_maior_q_x = int(input('Digite outro número decimal maior que X: '))
            print(numero_float_maior_q_x)
            
        else:
            print(f'{numero_float_maior_q_x} não é maior que {numero_x}')
            numero_float_maior_q_x = int(input('Digite outro número: '))

programa_float_maior_q_x = float_maior_q_x()


# letra D)
def float_max_x():
    numero_x = float(input('atribua um valor a X: '))
    numero_float_max_x = int(input('Digite um número positivo menor que X: '))
    while True:
        print(f'valor atribuido a X: {numero_x}')
        if numero_float_max_x <= numero_x:
            numero_float_max_x = int(input('Digite outro número decimal menor que X: '))
            print(numero_float_max_x)
            
        else:
            print(f'{numero_float_max_x} é maior que {numero_x}')
            numero_float_max_x = int(input('Digite outro número: '))


programa_float_max_x = float_max_x()


# Letra e)
def float_faixa_xy():
    numero_x = float(input('atribua um valor mínimo a X: '))
    numero_y = float(input('atribua um valor máximo a Y: '))
    numero_faixa_xy = float(input('Digite que esteja na faixa X e Y: '))
    while True:
        print(f'Faixa definida ({numero_x} a {numero_y})')
        if numero_x <= numero_faixa_xy <= numero_y:
            numero_faixa_xy = float(input('Digite outro número decimal no intervalo X - Y: '))
            print(numero_faixa_xy)
            
        else:
            print(f'{numero_faixa_xy} está fora de faixa [{numero_x} - {numero_y}]')
            numero_faixa_xy = float(input('Digite outro número: '))

programa_faixa_xy = float_faixa_xy()