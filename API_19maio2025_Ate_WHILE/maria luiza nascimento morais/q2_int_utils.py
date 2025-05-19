# A) 
def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a = int(entrada)
        return numero_a
    except ValueError:
        print('Valor Inteiro Inválido!')
        return get_integer_number(label)
    
# B) 
def get_int_positive(label: str):
    numero = get_integer_number(label)

    while numero < 0:
        print('O número deve ser positivo!')
        numero = get_integer_number(label)
    return numero

# C) 
def get_integer_number_min(label: str, min_value: int):
    numero = get_integer_number(label)

    while numero < min_value:
        print(f'O número deve ser no mínimo {min_value}')
        numero = get_integer_number(label)
    return numero

# D)
def get_integer_number_max(label: str, max_value: int):
    numero = get_integer_number(label)

    while numero > max_value:
        print(f'O número deve ser no máximo {max_value}')
        numero = get_integer_number(label)
    return numero

# E) 
def get_integer_in_range(label: str, min_value: int, max_value: int):
    numero = get_integer_number(label)

    while numero < min_value or numero > max_value:
        print(f'Valor fora da faixa ({min_value}-{max_value})')
        numero = get_integer_number(label)
    return numero
