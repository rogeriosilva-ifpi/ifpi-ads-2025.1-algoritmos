def obter_numero_inteiro(label: str):
    try:
        num = int(input(label))
        return num
    except ValueError:
        print('O número digitado não é um inteiro válido!')
        return obter_numero_inteiro(label)


def obter_numero_inteiro_positivo(label: str):
    numero = obter_numero_inteiro(label)

    if numero >= 0:
        return numero
    else:
        print(f'O valor deve ser positivo!')
        # faltou return
        obter_numero_inteiro_min(label)


def obter_numero_inteiro_min(label: str, min_value: int):
    numero = obter_numero_inteiro(label)

    if numero >= min_value:
        return numero
    else:
        print(f'O valor deve ser no mínimo {min_value}!')
        obter_numero_inteiro_min(label, min_value)


def obter_numero_inteiro_max(label: str, max_value: int):
    numero = obter_numero_inteiro(label)

    if numero <= max_value:
        return numero
    else:
        print(f'O valor deve ser no máximo {max_value}!')
        obter_numero_inteiro_min(label, max_value)


def obter_numero_inteiro_min_max(label: str, min_value: int, max_value: int):
    numero = obter_numero_inteiro(label)

    if numero < min_value or numero > max_value:
        print(f'O valor deve estar entre {min_value} e {max_value}!')
        # faltou return
        obter_numero_inteiro_min_max(label, min_value, max_value)