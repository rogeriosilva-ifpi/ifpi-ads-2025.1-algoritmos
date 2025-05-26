from q3_float_utils import obter_num_float
from q2_int_utils import obter_num_inteiro

#  No geral faltou compreender a questão e usar melhor funcoes para limpar o código.
# Lógica confusa

def main():

    print('>>>CALCULAR EMPRÉSTIMO<<<')

    # obter float min
    renda_mensal = obter_num_float('Informe sua renda mensal(R$): ')

    if renda_mensal < 0:
        print('Informe uma entrada válida')
        renda_mensal = obter_num_float('Informe sua renda mensal(R$): ')
    else:
        pass
    # acima a validação deve ser feita numa função .. para ficar em loop até encontra rum valor adequado

    valor_emprestimo = obter_num_float('Informe o valor do empréstimo(R$): ')
    if valor_emprestimo < 1518.00 or valor_emprestimo > (renda_mensal*0.3):
        # O limite de 30% é no valor da prestação e não no valor da renda e empréstimo
        print('Insira uma entrada válida')
        valor_emprestimo = obter_num_float('Informe o valor do empréstimo(R$): ')
    else:
        pass

    parcelas = obter_num_inteiro('Informe em quantas parcelas deseja dividir o empréstimo: ')
    # usar funções obter inteiro na faixa.
    if parcelas <= 0 or parcelas > 24:
        print('Insira uma entrada válida')
        parcelas = obter_num_inteiro('Informe em quantos meses deseja dividir o empréstimo: ')
    else:
        pass



    valor_iof = calcular_iof(valor_emprestimo, parcelas)
    # printar resultado no final.. lembra do Entrada/Proc/Saída
    print(f'Valor do IOF: R${valor_iof:.2f}')

    capital_inicial_juros = valor_emprestimo + valor_iof
    # esse cálculo abaixo tá sem sentido.
    selic = 14.75 * valor_emprestimo
    juros = calcular_juros(capital_inicial_juros, selic, parcelas)
    print(f'Valor dos juros a pagar: R${juros:.2f}')

    total_pagar = capital_inicial_juros + juros
    print(f'Valor total a pagar: R${total_pagar}')

    valor_mensal_parcela = total_pagar / parcelas
    print(f'Valor da parcela mensal: R${valor_mensal_parcela:.2f}')
    
    if renda_mensal < valor_mensal_parcela:
        print('Empréstimo recusado, renda mensal do cliente não suporta o valor da parcela')
    else:
        print('Empréstimo realizado com sucesso!')




def calcular_iof(valor_emprestimo, parcelas):
    prazo_desejado_dias = parcelas * 30
    iof = (0.38*valor_emprestimo) + (0.0082*prazo_desejado_dias)
    return iof


def calcular_juros(capital_inicial_juros, selic, parcelas):
    
    if parcelas <= 6:
        taxa = 0.5 * selic
    elif parcelas <= 12:
        taxa = 0.75 * selic
    elif parcelas <= 18:
        taxa = selic
    elif parcelas > 18:
        taxa = 1.30 * selic
    
    # calculou a taxa e não fez nada com ela.

    valor_juros = capital_inicial_juros * selic * parcelas
    return valor_juros



main()