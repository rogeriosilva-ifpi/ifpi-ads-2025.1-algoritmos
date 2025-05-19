# Recebendo um número float
def obter_numero_float(num):
    try: 
        if num != int(num):
            return num
        else:
            return 'Valor inválido'
    except ValueError:
        return 'Caractere inválido'


# Recebendo um número float positivo
def obter_numero_float_positivo(num):
    float = obter_numero_float(num)
    if float == num:
        if num > 0:
            return num
        return 'Número negativo inválido'
    return float
    

# Recebendo de no mínimo X
def obter_numero_float_min(num):
    min = 10.2
    float = obter_numero_float(num)
    if float == num:
        if num >= min:
            return num
        return f'Número menor que o mínimo {min}'
    return float


# Recebendo de no máximo X
def obter_numero_float_max(num):
    max = 25.6
    float = obter_numero_float(num)
    if float == num:
        if num <= max:
            return num
        return f'Número maior que o máximo {max}'
    return float


# Recebendo número float na faixa min X e max Y
def obter_numero_float_intervalo(num):
    min = 10.2
    max = 35.5
    float = obter_numero_float(num)
    if float == num:
        if min <= num <= max:
            return num
        return f'Número fora do intervalo de {min} e {max}'
    return float
