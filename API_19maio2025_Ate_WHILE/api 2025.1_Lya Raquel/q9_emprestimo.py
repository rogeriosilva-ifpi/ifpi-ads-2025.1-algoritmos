# bem confuso..
def main():
    renda = float(input('Renda mensal: '))
    emprestimo = float(input('Valor do empréstimo: '))
    prazo = int(input('Prazo de parcelamento: '))

    dias = prazo * 30
    parcela_renda = (30 / 100) * renda

    valor_iof = iof(emprestimo, dias)
    selic = juros_selic(emprestimo)
    total_juros = juros(selic, prazo, emprestimo, valor_iof)
    total_parcela = parcelas(emprestimo, total_juros, prazo)
    resultado_emprestimo = aprovado_negado(parcela_renda, total_parcela)

    total_pagar = emprestimo + total_juros

    while True:
        if emprestimo < 1518.00:
            print('O valor mínimo para empréstimo é de um sálario mínimo.')
            emprestimo = float(input('Valor do empréstimo: '))
        break

    tela(valor_iof, total_juros, prazo, total_parcela, total_pagar, resultado_emprestimo)

def juros_selic(emprestimo):
    juros = (14.75 / 100) * emprestimo
    return juros

def juros(selic, prazo, emprestimo, valor_iof):
    if prazo <= 6:
        total_selic = (50 / 100) * selic
        total_juros = total_selic + valor_iof
        return total_juros
    elif prazo == 7 and prazo < 12:
        total_selic = (75 / 100) * selic
        total_juros = total_selic + valor_iof
        return total_juros
    elif prazo == 12 and prazo < 18:
        total_juros = selic + valor_iof
        return total_juros
    elif prazo > 18:
        total_selic = (130 / 100) * selic
        total_juros = total_selic + valor_iof
        return total_juros


def parcelas(emprestimo, total_juros, prazo):
    valor_parcela = (emprestimo + total_juros ) / prazo
    return valor_parcela


def iof(emprestimo, dias):
    valor = (0.38 / 100) * emprestimo
    valor2 = ((0.0082 / 100) * emprestimo) * dias
    total_iof = valor + valor2
    return total_iof

def minmax_parcelas(prazo):
    if prazo < 2:
        print('O prazo mínimo são de 2 parcelas.')
    elif prazo > 24:
        print('O empréstimo só pode ser parcelado até 24x.')

def aprovado_negado(parcela_renda, total_parcela):
    if total_parcela <= parcela_renda:
        return 'APROVADO!'
    else:
        return 'NEGADO!'



def tela(valor_iof, total_juros, prazo, total_parcela, total_pagar, resultado_emprestimo):
    inf = f'''
    RSBank
    Valor do IOF: R$ {valor_iof:.2f}
    Valor dos Juros a pagar: R$ {total_juros:.2f}
    Valor total a pagar: R$ {total_pagar:.2f}
    Valor da parcela mensal: {prazo}x de R$ {total_parcela:.2f}
    Empréstimo: {resultado_emprestimo}
'''
    print(inf)

main()
