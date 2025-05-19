def main():
    num_n = get_integer_number_min('Número N: ', 0)
    num_m = get_integer_number_min('Número M: ', 0)
    while num_n <= num_m:
        contador = 1
        soma = 0
        while contador <= num_n:
            if num_n % contador == 0:
                soma += num_n/contador
                
                if num_n == soma:
                    print(f'{num_n} é um número perfeito')
                else:
                    print(f'{num_n} não é um número perfeito')
            contador += 1
        num_n += 1





def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a = int(entrada)
        return numero_a
    except ValueError:
        print('Valor Inteiro Inválido!')
        return get_integer_number(label)
    

def get_integer_number_min(label: str, min_value: int):
    numero = get_integer_number(label)

    while numero < min_value:
        print(f'O número deve ser no mínimo {min_value}')
        numero = get_integer_number(label)
    return numero

main()