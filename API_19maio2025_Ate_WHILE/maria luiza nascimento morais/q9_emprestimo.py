

def main():
    renda_mensal = get_decimal_number_min('Renda mensal: ', 0)
    valor_emprestimo = get_decimal_number_min('Valor empréstimo: ', 1518)
    prazo = get_integer_in_range('Prazo: ', 2,24)

    iof = (valor_emprestimo * 0.38) + ((0.0082/100) * (prazo * 30))
    valor_total_pagar = (valor_emprestimo + iof) * (1 + selic(prazo))
    juros = valor_total_pagar - valor_emprestimo
    parcela = valor_total_pagar/prazo

    emprestimo_interface = f'''=== CÁLCULO DE EMPRÉSTIMO ===
VALOR DO IOF: R${iof:.2f}
VALOR DOS JUROS A PAGAR: R$ {juros:.2f}
VALOR TOTAL A PAGAR: R$ {valor_total_pagar:.2f}
VALOR DA PARCELA MENSAL: {prazo}x de R$ {parcela:.2f}
SITUAÇÃO DO EMPRÉSTIMO: {validar_emprestimo(parcela, renda_mensal)}
'''
    print(emprestimo_interface)



def validar_emprestimo(parcela: float, renda_mensal: float):
    if parcela > renda_mensal * 0.3:
        return 'EMPRÉSTIMO NEGADO'
    else:
        return 'EMPRÉSTIMO APROVADO'


def selic(prazo):
    if prazo <= 6:
        return 14.75/100 * 0.5
    elif prazo <= 12:
        return 14.75/100 * 0.75
    elif prazo <= 18:
        return 14.75/100 
    else:
        return 14.75/100 * 1.3


def get_decimal_number_min(label: str, min_value: int):
    numero = get_decimal_number(label)

    while numero < min_value:
        print(f'O número deve ser no mínimo {min_value}')
        numero = get_decimal_number(label)
    return numero


def get_decimal_number(label: str):
    entrada = input(label)

    try:
        numero_a = float(entrada)
        return numero_a
    except ValueError:
        print('Valor Decimal Inválido!')
        return get_decimal_number(label)
    

def get_integer_in_range(label: str, min_value: int, max_value: int):
    numero = get_integer_number(label)

    while numero < min_value or numero > max_value:
        print(f'Valor fora da faixa ({min_value}-{max_value})')
        numero = get_integer_number(label)
    return numero


def get_integer_number(label: str):
    entrada = input(label)

    try:
        numero_a = int(entrada)
        return numero_a
    except ValueError:
        print('Valor Inteiro Inválido!')
        return get_integer_number(label)
    
main()