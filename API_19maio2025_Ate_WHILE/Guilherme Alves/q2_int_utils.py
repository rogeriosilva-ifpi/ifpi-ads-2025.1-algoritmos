def obter_int(label:str):
    entrada = input(label)
    try:
        num = int(entrada)
        return num
    except:
        print("Digite um número inteiro válido")
        return obter_int(label)

def obter_int_positivo(label:str):
    num = obter_int(label)
    if num > 0:
        return num
    else:
        print("Digite um número inteiro positivo")
        return obter_int_positivo(label)

def obter_int_min(label:str,min:int):
    num = obter_int(label)
    if min <= num:
        return num
    else:
        print(f"O número deve ser no mínimo: {min}")
        return obter_int_min(label,min)

def obter_int_max(label:str,max:int):
    num = obter_int(label)
    if num <= max:
        return num
    else:
        print(f"O número deve ser no maxímo: {max}")
        return obter_int_max(label,max)

def obter_int_min_e_max(label:str,min:int,max:int):
    num = obter_int(label)
    if min <= num <= max:
        return num
    else:
        print(f"O número deve ser no mínimo: {min} e no maxímo: {max}")
        return obter_int_min_e_max(label,min,max)