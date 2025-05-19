# A) 
def get_decimal_number(label: str):
    entrada = input(label)

    try:
        numero_a = float(entrada)
        return numero_a
    except ValueError:
        print('Valor Decimal Inválido!')
        return get_decimal_number(label)
    
# B) 
def get_decimal_positive(label: str):
    numero = get_decimal_number(label)

    while numero < 0:
        print('O número deve ser positivo!')
        numero = get_decimal_number(label)
    return numero

# C) 
def get_decimal_number_min(label: str, min_value: int):
    numero = get_decimal_number(label)

    while numero < min_value:
        print(f'O número deve ser no mínimo {min_value}')
        numero = get_decimal_number(label)
    return numero

# D)
def get_decimal_number_max(label: str, max_value: int):
    numero = get_decimal_number(label)

    while numero > max_value:
        print(f'O número deve ser no máximo {max_value}')
        numero = get_decimal_number(label)
    return numero

# E) 
def get_decimal_in_range(label: str, min_value: int, max_value: int):
    numero = get_decimal_number(label)

    while numero < min_value or numero > max_value:
        print(f'Valor fora da faixa ({min_value}-{max_value})')
        numero = get_decimal_number(label)
    return numero
