# Obtendo texto
def obtendo_str(text):
    try:
        if text == str(text):
            return text
        return f'{text} não é um texto str()'
    except ValueError:
        return 'Caractere Inválido'


# Obtendo texto tamanho minimo 
def obtendo_str_min(text):
    min = 5
    texto = obtendo_str(text)
    if texto == text:
        if len(text) >= min:
            return text
        return f'{text} abaixo do mínimo {min}'
    return texto


# Obtendo texto tamanho máximo 
def obtendo_str_max(text):
    max = 10
    texto = obtendo_str(text)
    if texto == text:
        if len(text) <= max:
            return text
        return f'{text} acima do máximo {max}'
    return texto


# Obtendo o texto em um intervalo max e min
def obtendo_str_intevalo(text):
    max = 15
    min = 5
    texto = obtendo_str(text)
    if texto == text:
        if min <= len(text) <= max:
            return text
        return f'{text} fora do intervalo de {min} e {max}'
    return texto 