def obter_num_float(label: str):
    entrada = input(label)
    try:
        num = float(entrada)
        return num
    except ValueError:
        print('Entrada inválida, escreva um valor númerico. Tente novamente: ')
        return obter_num_float(label)
    

def obter_numero_float_positivo(label: str):
    entrada = input(label)
    try:
        num = float(entrada)
        if num >= 0:
            return num
        else:
            print('Valor inválido, escreva um número positivo. Tente novamente: ')
            return obter_numero_float_positivo(label)
    except ValueError:
        print('Entrada inválida, escreva um valor númerico. Tente novamente: ')
        return obter_numero_float_positivo(label)
    

def obter_numero_float_min(label: str, min: float):
    entrada = input(label)
    try:
        num = float(entrada)
        if num >= min:
            return num
        else:
            print(f'Valor inválido, escreva um número maior ou igual a {min}. Tente novamente: ')
            return obter_numero_float_min(label, min)
    except ValueError:
        print('Entrada inválida, escreva um valor númerico. Tente novamente: ')
        return obter_numero_float_min(label, min)  
    

def obter_numero_float_max(label: str, max: float):
    entrada = input(label)
    try:
        num = float(entrada)
        if num <= max:
            return num
        else:
            print(f'Valor inválido, escreva um número menor ou igual a {max}. Tente novamente: ')
            return obter_numero_float_max(label, max)
    except ValueError:
        print('Entrada inválida, escreva um valor númerico. Tente novamente: ')
        return obter_numero_float_max(label, max) 


def obter_numero_float_em_faixa(label: str, min: float,max: float):
    entrada = input(label)
    try:
        num = float(entrada)
        if num >= min and num <= max:
            return num
        else:
            print(f'Valor inválido, escreva um número entre {min} e {max}. Tente novamente: ')
            return obter_numero_float_em_faixa(label, min, max)
    except ValueError:
        print('Entrada inválida, escreva um valor númerico. Tente novamente: ')
        return obter_numero_float_em_faixa(label, min, max)