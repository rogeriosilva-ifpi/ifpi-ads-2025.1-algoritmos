import os
from q2_int_utils import obter_numero_int_positivo

def main():
    qtd_familias = obter_numero_int_positivo('Números de famílias: ')
    contador = qtd_familias
    talao_geral = f"""
 ======== TALÃO MENSAL XPTO ========
 """

    while contador > 0:
        limpar_tela()
        consumidor = input('Consumidor: ')
        consumo = obter_numero_int_positivo('Consumo(KWh): ')
        
        valor_consumo = calcular_valor_consumo(consumo)
        taxa_iluminacao = calcular_taxa_iluminacao(valor_consumo)
        valor_fatura = valor_consumo + taxa_iluminacao
        icms = (25/100) * valor_fatura
        pis_cofins = (3.75/100) * valor_fatura
        valor_total = valor_fatura + icms + pis_cofins + taxa_iluminacao

        talao_individual = f"""
 ------------------------------
 Consumidor: {consumidor}
 Consumo(KWh): {consumo}
 Consumo(R$): R$ {valor_consumo:.2f}
 ICMS: {icms:.2f}
 PIS/COFINS: {pis_cofins:.2f}
 Taxa iluminação pública: {taxa_iluminacao:.2f}

 TOTAL A PAGAR: R${valor_total:.2f}
 """
        talao_geral += talao_individual
        contador -= 1
    
    print(talao_geral)

def calcular_valor_consumo(consumo):
    if consumo <= 30:
        return 0
    elif consumo <= 200:
        return 0.89 * consumo
    else:
        return (0.89 * 1.3) * consumo
    
def calcular_taxa_iluminacao(valor_consumo):
    if valor_consumo == 0:
        return 0
    else:
        return (3/100) * valor_consumo

def limpar_tela():
    os.system('cls')

main()