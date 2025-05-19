def main():
    qtd_familias = get_integer_number_min('Quantidade de famílias: ',0)
    contador = 0

    while contador < qtd_familias:
        nome = str(input('Nome do cliente: '))
        consumo = get_integer_number_min('Consumo(KWh): ', 0)
        contador += 1


        fatura_sem_imposto = consumo_reais(consumo) + bandeira(consumo)
        icms = (fatura_sem_imposto + iluminacao(consumo)) * 25/100
        pis_confins = (fatura_sem_imposto + iluminacao(consumo)) * 3.75/100
        fatura_total = (fatura_sem_imposto + iluminacao(consumo)) + icms + pis_confins

        extrato = f'''=== TALÃO MENSAL XPTO ===
CONSUMIDOR: {nome}
CONSUMO(KWH): {consumo}
CONSUMO(R$): R${consumo_reais(consumo):.2f} 
BANDEIRA TARIFÁRIA: R$ {bandeira(consumo):.2f} 
TOTAL SEM IMPOSTOS: R${fatura_sem_imposto:.2f} 
ICMS: R${icms:.2f}
PIS/CONFINS: R${pis_confins:.2f}
ILUMINAÇÃO PÚBLICA: R${iluminacao(consumo):.2f}
-------------------------------------------------------
VALOR TOTAL A PAGAR: R${fatura_total:.2f}

'''
        print(extrato)
    

def bandeira(consumo: int):
    if consumo_reais(consumo) > 0:
        return (consumo/100) * 0.89
    else:
        return 0
    

def consumo_reais(consumo: int) -> float:
    if consumo <= 30:
        return 0
    elif consumo < 200:
        return consumo * 0.89
    else:
        return consumo * (0.89 * 1.3)


def iluminacao(consumo: int) -> float:
    if consumo_reais(consumo) > 0:
        return consumo * 0.03
    else:
        return 0


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