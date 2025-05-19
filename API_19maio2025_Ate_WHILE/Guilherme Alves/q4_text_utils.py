def obter_texto(label:str):
    entrada = input(label)
    try:
        texto = str(entrada)
        return texto
    except:
        print("Digite um texto")
        return obter_texto(label)

def obter_texto_min(label:str,min:int):
    texto = obter_texto(label)
    if min <= len(texto):
        return texto
    else:
        print(f"O texto deve ter tamanho de no mínimo: {min}")
        return obter_texto_min(label,min)

def obter_texto_max(label:str,max:int):
    texto = obter_texto(label)
    if len(texto) <= max:
        return texto
    else:
        print(f"O texto deve ter tamanho de no maxímo: {max}")
        return obter_texto_max(label,max)

def obter_texto_min_e_max(label:str,min:int,max:float):
    texto = obter_texto(label)
    if min <= len(texto) <= max:
        return texto
    else:
        print(f"O texto deve ter tamanho de no mínimo: {min} e no maxímo: {max}")
        return obter_texto_min_e_max(label,min,max)
