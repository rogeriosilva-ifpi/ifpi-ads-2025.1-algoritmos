def obter_texto(label:str):
    texto = input(label)
    return texto


def obter_texto_min(label,limite_min):
    entrada = obter_texto(label)

    if len(entrada) >= limite_min:
        return entrada
    else:
        print(f'O texto é menor que o limite de {limite_min} caracteres. Tente novamente!')
        return obter_texto_min(label, limite_min)


def obter_texto_max(label, limite_max):
    entrada = obter_texto(label)

    if len(entrada) <= limite_max:
        return entrada
    else:
        print(f'O texto é  excede o limite de {limite_max} caracteres. Tente novamente!')
        return obter_texto_max(label, limite_max)


def obter_texto_in_faixa(label, limite_min, limite_max):
    entrada = obter_texto(label)

    if len(entrada) >= limite_min and len(entrada) <= limite_max:
        return entrada
    else:
        print(f'O texto está fora da faixa de {limite_min} à {limite_max} caracteres. Tente novamente!')
        return obter_texto_in_faixa(label, limite_min, limite_max)

