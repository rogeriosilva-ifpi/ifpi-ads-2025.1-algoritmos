def obter_num_inteiro(label: str):
    entrada = input(label)
    try:
        num = int(entrada)
        return num
    except ValueError:
        print('Entrada inválida, escreva um valor númerico e inteiro. Tente novamente: ')
        return obter_num_inteiro(label)
    

def obter_numero_int_positivo(label: str):
    entrada = input(label)
    try:
        num = int(entrada)
        if num >= 0:
            return num
        else:
            print('Valor inválido, escreva um número positivo. Tente novamente: ')
            return obter_numero_int_positivo(label)
    except ValueError:
        print('Entrada inválida, escreva um valor númerico e inteiro. Tente novamente: ')
        return obter_numero_int_positivo(label)
    

def obter_numero_int_min(label: str, min: int):
    entrada = input(label)
    try:
        num = int(entrada)
        if num >= min:
            return num
        else:
            print(f'Valor inválido, escreva um número maior ou igual a {min}. Tente novamente: ')
            return obter_numero_int_min(label, min)
    except ValueError:
        print('Entrada inválida, escreva um valor númerico e inteiro. Tente novamente: ')
        return obter_numero_int_min(label, min)  
    

def obter_numero_int_max(label: str, max: int):
    entrada = input(label)
    try:
        num = int(entrada)
        if num <= max:
            return num
        else:
            print(f'Valor inválido, escreva um número menor ou igual a {max}. Tente novamente: ')
            return obter_numero_int_max(label, max)
    except ValueError:
        print('Entrada inválida, escreva um valor númerico e inteiro. Tente novamente: ')
        return obter_numero_int_max(label, max) 


def obter_numero_int_em_faixa(label: str, min: int,max: int):
    entrada = input(label)
    try:
        num = int(entrada)
        if num >= min and num <= max:
            return num
        else:
            print(f'Valor inválido, escreva um número entre {min} e {max}. Tente novamente: ')
            return obter_numero_int_em_faixa(label, min, max)
    except ValueError:
        print('Entrada inválida, escreva um valor númerico e inteiro. Tente novamente: ')
        return obter_numero_int_em_faixa(label, min, max)