def obter_numero_decimal(label: str):
    try:
        num = int(input(label))
        return num
    except ValueError:
        print('O número digitado não é um decimal válido!')
        return obter_numero_decimal(label)


def obter_numero_decimal_positivo(label: str):
    numero = obter_numero_decimal(label)

    if numero >= 0:
        return numero
    else:
        print(f'O valor deve ser positivo!')
        obter_numero_decimal_min(label)


def obter_numero_decimal_min(label: str, min_value: int):
    numero = obter_numero_decimal(label)

    if numero >= min_value:
        return numero
    else:
        print(f'O valor deve ser no mínimo {min_value}!')
        obter_numero_decimal_min(label, min_value)


def obter_numero_decimal_max(label: str, max_value: int):
    numero = obter_numero_decimal(label)

    if numero <= max_value:
        return numero
    else:
        print(f'O valor deve ser no máximo {max_value}!')
        obter_numero_decimal_min(label, max_value)


def obter_numero_decimal_min_max(label: str, min_value: int, max_value: int):
    numero = obter_numero_decimal(label)

    if numero < min_value or numero > max_value:
        print(f'O valor deve estar entre {min_value} e {max_value}!')
        obter_numero_decimal_min_max(label, min_value, max_value)