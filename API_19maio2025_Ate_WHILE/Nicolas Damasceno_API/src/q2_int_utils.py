# Recebendo um número inteiro
def obter_numero_inteiro(descricao):
    # Não tá retornando sempre um inteiro válido. tá retornando texto
    valor = input(descricao)
    try: 
        num = int(valor)
        return num
    except ValueError:
        return obter_numero_inteiro(descricao)


# Recebendo um número inteiro positivo
def obter_numero_inteiro_positivo(descricao):
    numero = obter_numero_inteiro(descricao)

    while numero <= 0:
        numero = obter_numero_inteiro(descricao)

    return numero
    

# Recebendo de no mínimo X
def obter_numero_inteiro_min(num):
    min = 10
    inteiro = obter_numero_inteiro(num)
    if inteiro == num:
        if num >= min:
            return num
        return f'Número menor que o mínimo {min}'
    return inteiro


# Recebendo de no máximo X
def obter_numero_inteiro_max(num):
    max = 25
    inteiro = obter_numero_inteiro(num)
    if inteiro == num:
        if num <= max:
            return num
        return f'Número maior que o máximo {max}'
    return inteiro


# Recebendo número inteiro na faixa min X e max Y
def obter_numero_inteiro_intervalo(num):
    min = 10
    max = 35
    inteiro = obter_numero_inteiro(num)
    if inteiro == num:
        if min <= num <= max:
            return num
        return f'Número fora do intervalo de {min} e {max}'
    return inteiro