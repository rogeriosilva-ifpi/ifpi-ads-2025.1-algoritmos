def obter_real(label:str):
    entrada = input(label)
    try:
        num = float(entrada)
        return num
    except:
        print("Digite um número decimal válido")
        return obter_real(label)

def obter_real_positivo(label:str):
    num = obter_real(label)
    if num > 0:
        return num
    else:
        print("Digite um número real positivo")
        return obter_real_positivo(label)

def obter_real_min(label:str,min:float):
    num = obter_real(label)
    if min <= num:
        return num
    else:
        print(f"O número deve ser no mínimo: {min}")
        return obter_real_min(label,min)

def obter_real_max(label:str,max:float):
    num = obter_real(label)
    if num <= max:
        return num
    else:
        print(f"O número deve ser no maxímo: {max}")
        return obter_real_max(label,max)

def obter_real_min_e_max(label:str,min:float,max:float):
    num = obter_real(label)
    if min <= num <= max:
        return num
    else:
        print(f"O número deve ser no mínimo: {min} e no maxímo: {max}")
        return obter_real_min_e_max(label,min,max)