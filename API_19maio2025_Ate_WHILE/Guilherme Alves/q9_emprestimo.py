from q3_float_utils import obter_real,obter_real_min
from q2_int_utils import obter_int_min_e_max
def main():

    renda_mensal = obter_real("Informe a sua renda mensal(em R$): ")
    valor_emp = obter_real_min("Informe o valor do empréstimo(em R$): ",1518)
    prazo = obter_int_min_e_max("Digite a quantidade de tempo em que deseja pegar(em meses com uma tabela por mês): ",2,24)

    selic = calc_selic(prazo)

    iof = calc_iof(valor_emp,prazo)
    juros = calc_juros(valor_emp,iof,selic,prazo)
    valor_total = valor_emp + juros
    parcela = valor_total / prazo
    
    if ((parcela / renda_mensal) * 100) <= 30:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"
        
    resultado = f'''
    >>>> Dados do empréstimo: <<<<
    Valor do IOF: {iof:.2f} R$
    Valor dos juros a pagar: {juros:.2f} R$
    Valor total a pagar: {valor_total:.2f} R$
    Valor da parcela mensal: {parcela:.2f} R$
    Situação do empréstimo: {situacao}
    '''

    print(resultado)

def calc_iof(valor_emp,prazo):
    iof = (valor_emp * (0.38/100)) + ((0.0082/100) * (prazo * 30))
    return iof

def calc_selic(prazo):
    if prazo <= 6:
        selic = ((14.75/100) * 0.5) / 12
    elif prazo <= 12:
        selic = ((14.75/100) * 0.75) / 12
    elif prazo <= 18:
        selic = ((14.75/100) * 1) / 12
    else:
        selic = ((14.75/100) * 1.3) / 12
    return selic

def calc_juros(valor_emp,iof,selic,prazo):
    juros = (valor_emp + iof) * (selic) * (prazo)
    return juros

main()