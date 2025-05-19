def calcular_iof(valor_total , meses):
    dias = meses*30
    iof = (valor_total*0.0038) + (valor_total*0.000082*dias)
    return iof

def calcular_juros(prazo , valor_total ):
    selic = 14.75

    if(prazo <= 6 ):
        juros = valor_total*1/2*selic*prazo
        return juros
    
    if(prazo>=7 and prazo<=12):
        juros = valor_total*3/4*selic*prazo
        return juros

    if(prazo >= 12 and prazo <= 18):
        juros = valor_total*selic*prazo
        return juros
    
    if(prazo > 18):
        juros = valor_total*13/10*selic*prazo
        return juros

def aprovacao_emprestimo(renda_mensal , parcela):
    if(parcela < 0.3*renda_mensal):
        return True
    return False


def main():
    renda_mensal = float(input('Qual sua renda mensal ? '))
    valor_emprestimo = float(input('Qual valor do emprestimo? '))
    prazo = int(input('Em quantos meses deseja pagar ? '))
    limite_parcela = 0.3*renda_mensal

    iof = calcular_iof(valor_emprestimo, prazo)
    juros = calcular_juros(prazo , valor_emprestimo)
    total_a_pagar = valor_emprestimo + juros + iof
    parcela_mensal = total_a_pagar/prazo
    aprovado = aprovacao_emprestimo(renda_mensal,parcela_mensal)

    if aprovado:
        print('EMPRESTIMO APROVADO')
        print(f'Valor IOF: R${iof}')
        print(f'Valor juros: R${juros}')
        print(f'Total a pagar: R${total_a_pagar}')
        print(f'Parcela mensal: R${parcela_mensal}')
    else:
        print('EMPRESTIMO REPROVADO')

main()