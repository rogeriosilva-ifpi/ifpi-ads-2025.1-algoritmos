def obter_texto(label: str):
    try:
        texto = input(label)
        return texto
    except ValueError:
        print('O valor deve ser uma string!')
        return obter_texto(label)


def obter_texto_min(label: str, min_value: int):
    texto = obter_texto(label)

    if len(texto) >= min_value:
        return texto
    else:
        print(f'O tamanho deve ser de no mínimo {min_value} letras!')
        obter_texto_min(label, min_value)


def obter_texto_max(label: str, max_value: int):
    texto = obter_texto(label)

    if len(texto) < max_value:
        return texto
    else:
        print(f'O valor deve ser de no máximo {max_value} letras!')
        obter_texto_max(label, max_value)


def obter_texto_min_max(label: str, min_value: int, max_value: int):
    texto = obter_texto(label)

    if len(texto) < min_value or len(texto) > max_value:
        print(f'O valor deve estar entre {min_value} e {max_value} letras!')
        obter_texto_min_max(label, min_value, max_value)