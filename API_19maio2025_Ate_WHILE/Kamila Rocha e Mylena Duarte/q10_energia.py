from q2_int_utils import receber_int_positivo
from q4_text_utils import obter_texto


def main():
    saida = '**** TALÃO MENSAL XPTO ****'
    n_familias = receber_int_positivo('Digite a quantidade de familias: ')
    while True:
        nome = obter_texto('Digite o nome do consumidor: ')
        saida += f'\n Consumidor: {nome}'
        n_familias -= 1
        consumo_familia = receber_int_positivo(
            'Digite o consumo da sua família: ')
        saida += f'\nConsumo (Kwh): {consumo_familia:.2f}'
        if n_familias == 0:
            break

        if consumo_familia <= 30:
            valor_kwh = 0
        elif consumo_familia >= 200:
            porcentagem = (0.89/30)*100
            valor_kwh = porcentagem
        else:
            valor_kwh = 0.89
        saida += f'\nConsumo (R$): {valor_kwh:.2f}'

        valor_fatura = consumo_familia * valor_kwh
        saida += f'\nTotal sem impostos: {valor_fatura}'

        if valor_fatura > 0:
            tarifa_iluminacao = (valor_fatura / (3/100))
        else:
            tarifa_iluminacao = 0
        
        saida += f'\nTarifa iluminação: {tarifa_iluminacao}'

        ICMS = (valor_fatura / 25) * 100
        saida += f'\nICMS: {ICMS:.2F}'
        PIS_confins = (valor_fatura/3.75) * 100
        saida += f'\nPIS/CONFINS: {PIS_confins:.2F}'

        total_pagar = valor_fatura + tarifa_iluminacao + ICMS + PIS_confins
        saida += f'\ntotal a pagar: {total_pagar:.2f}'
        
    print(saida)


main()
