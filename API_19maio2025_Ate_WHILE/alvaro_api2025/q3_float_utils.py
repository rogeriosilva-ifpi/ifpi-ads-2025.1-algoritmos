
# mesmos problemas da int utils
def obter_num_float(label:str):
    return float(input(label))

def obter_num_float_positivo(label:str):
    num = float(input(label))
    if num < 0:
        print('Insira um número positivo!')
        return obter_num_float_positivo(label)
    else:
        return f'{num:.2f}'
    
def obter_num_max_x(label:str):
    num = float(input('Insira um núemro para o limite máximo: '))
    new_num = float(input('Agora insira um número: '))
    if new_num > num:
        print(f'Número inválido, tente novamente')
        return obter_num_max_x(label)
    else:
        return f'{new_num:.2f}'
    
def obter_num_min_x(label:str):
    num = float(input('Informe um número para ser o limite mínimo: '))
    new_num = float(input('Agora insira um número: '))
    if new_num < num:
        print('Número inválido, tente novamente')
        return obter_num_min_x(label)
    else:
        return f'{new_num:.2f}'
    
def obter_num_xy(label:str):
    numX = float(input('Informe um número para ser o limite mínimo: '))
    numY = float(input('Informe um número para ser o limte mínimo: '))
    new_num = float(input('Informe um número: '))
    if new_num < numX or new_num > numY:
        print('Número inválido, tente novamente')
        return obter_num_xy(label)
    else:
        return f'{new_num:.2f}'
