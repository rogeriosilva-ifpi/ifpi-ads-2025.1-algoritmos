
def obter_num_inteiro(label:str):
    return int(input(label))

def obter_num_inteiro_positivo(label:str):
    num = int(input(label))
    if num < 0:
        print('Insira um número positivo!')
        return obter_num_inteiro_positivo(label)
    else:
        return num
    
def obter_num_max_x(label:str):
    num = int(input('Insira um núemro para o limite máximo: '))
    new_num = int(input('Agora insira um número: '))
    if new_num > num:
        print(f'{new_num} é maior que {num}, tente novamente')
        return obter_num_max_x(label)
    else:
        return new_num
    
def obter_num_min_x(label:str):
    num = int(input('Informe um número para ser o limite mínimo: '))
    new_num = int(input('Agora insira um número: '))
    if new_num < num:
        print(f'{new_num} é menor que {num}, tente novamente')
        return obter_num_min_x(label)
    else:
        return new_num
    
def obter_num_xy(label:str):
    numX = int(input('Informe um número para ser o limite mínimo: '))
    numY = int(input('Informe um número para ser o limte mínimo: '))
    new_num = int(input('Informe um número: '))
    if new_num < numX or new_num > numY:
        print('Número inválido, tente novamente')
        return obter_num_xy(label)
    else:
        return new_num
