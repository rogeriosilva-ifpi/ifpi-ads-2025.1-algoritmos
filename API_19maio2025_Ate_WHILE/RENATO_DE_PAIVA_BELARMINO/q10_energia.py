


def main():
    valor_kwh = 0.89
    total_a_pagar = 0
    bandeira = 0
    n = int(input('Insira a quantidade de consumidores > '))
    i = 1
    while i <= n:
        consumidor = input('Insira o nome do consumidor > ')
        consumo = float(input('Insira quantidade consumo mensal (KWh) > '))
        if consumo <= 30:
             valor_kwh_caro = valor_kwh * 0.3
             valor_kwh = valor_kwh_caro
             consumo_pagar = consumo * valor_kwh
             iluminacao = consumo_pagar * 0.03
             icms = (consumo_pagar) * 0.025
             pins_cofins = (consumo_pagar) * 0.0375
             valor_total = 0
             valor_kwh = 0
        if consumo > 30 and consumo <= 200:
             consumo_pagar = consumo * valor_kwh
             iluminacao = consumo_pagar * 0.03
             icms = (consumo_pagar) * 0.025
             pins_cofins = (consumo_pagar) * 0.0375
             valor_total = icms + consumo_pagar + pins_cofins + iluminacao + bandeira
             
        elif consumo > 200:
             valor_kwh_caro = valor_kwh * 0.3
             valor_kwh = valor_kwh_caro
             consumo_pagar = consumo * valor_kwh
             iluminacao = consumo_pagar * 0.03
             icms = (consumo_pagar) * 0.025
             pins_cofins = (consumo_pagar) * 0.0375
             valor_total = icms + consumo_pagar + pins_cofins + iluminacao + bandeira
             
        print(f""""
                ---------TALÃO MENSAL XPTO----------
                Consumidor: {consumidor}
                Consumo (KWh): {consumo} (valor por KWh: R$ {valor_kwh})
                Bandeira tarifária: VERDE ( R$ 0,00)
                Total sem impostos: R$ {consumo_pagar:.2f}
                ICMS: R$ {icms:.2f}
                PIS/COFINS: R$ {pins_cofins:.2f}
                Iluminação pública: R$ {iluminacao:.2f}
                ---------------------------------------------------
                Total a pagar: R$ {valor_total:.2f}               
                """)
        i += 1





main()