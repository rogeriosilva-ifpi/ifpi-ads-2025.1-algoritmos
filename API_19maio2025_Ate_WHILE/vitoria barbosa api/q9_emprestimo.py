from q3_float_utils import obter_numero_float_em_faixa
from q2_int_utils import obter_numero_int_em_faixa

def main():
    # Entrada
    renda_mesal = obter_numero_float_em_faixa('Sua renda mensal: ', 1, 100000)
    valor_emprestimo = obter_numero_float_em_faixa('Valor do emprétimo: ', 1518, 100000)
    prazo = obter_numero_int_em_faixa('Prazo em que deseja pagar: ', 2, 24)
    # Processamento
    dias_prazo = prazo * 30
    iof = ((0.38/100) * valor_emprestimo) + ((0.0082/100) * dias_prazo)
    taxa_percentual = calcular_taxa(prazo)
    juros = (valor_emprestimo + iof) * (taxa_percentual/100) * prazo
    valor_total = valor_emprestimo + juros
    valor_parcela = valor_total / prazo
    situacao = analisar_situacao(valor_parcela, renda_mesal)
    # Saída
    print(f"""
 ======== SOLICITAÇÃO DE EMPRÉSTIMO ========
 > Valor do empréstimo: R$ {valor_emprestimo:.2f}
 > Prazo: {prazo}x
 > Valor IOF: R$ {iof:.2f}
 > Valor Juros: R$ {juros:.2f}
 > Valor Total: R$ {valor_total:.2f}
 > Valor da parcela mensal: {prazo}X de R$ {valor_parcela:.2f}

 > SITUAÇÃO: {situacao}
""")


def analisar_situacao(valor_parcela, renda_mensal):
    valor_max = (30/100) * renda_mensal
    if valor_parcela > valor_max:
        return 'REPROVADO. A parcela é maior que 30% da sua renda mensal'
    else:
        return 'APROVADO'


def calcular_taxa(prazo):
    if prazo <= 6:
        return (50/100) * 14.75
    elif prazo < 12:
        return (75/100) * 14.75
    elif prazo <= 18:
        return 14.75
    else:
        return (130/100) * 14.75

main()