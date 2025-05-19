import utils
import os
def main():
    utils.clear()

    nome_consumidor = input("Insira o nome do consumidor: ")
    kwh = int(input("Insira a quantidade de KWh consumida: "))
    bandeira = float(input("Insira o valor da bandeira em porcentagem (%): "))

    acrecimo = 1
    gasto = 0

    if kwh <= 30:
        utils.clear()
        return print("""****** TALÃO MENSAL XPTO ******
Consumidor: {nome_consumidor}
Consumo: (KWh): {kwh}
-----------------------------
Total a Pagar: R$ 0.00
insento  
""")
    elif kwh > 200:
        gasto = (kwh * 0.89) * 0.30
        gastokwh = gasto / kwh 
        tarifa = (kwh // 100) * bandeira
        ilum = (gasto * 0.03) 
        sem_imps = gasto + tarifa + ilum
        icms = (gasto * 0.25) 
        pis =  (gasto * 0.0375)
        total = gasto + ilum + icms + pis + bandeira
        utils.clear()
        print(f""" ****** TALÃO MENSAL XPTO ******
Consumidor: {nome_consumidor}
Consumo: (KWh): {kwh}
consumo (R$): R$ {gasto:.2f} (valor por KWh:R$ {gastokwh})
Bandeira da Taifária: R$ {tarifa}
total sem imposto: {sem_imps:.2f}
ICMS: R$ {icms:.2f}
PIS/COFINS: {pis:.2f}
iluminação publica: R$ {ilum:.2f}
-------------------------------------------------------
Total a Pagar: R$ {total}

""")
    else:
        gasto = kwh * 0.89
        gastokwh = gasto / kwh 
        ilum = (gasto * 0.03) 
        tarifa = (kwh // 100) * bandeira
        sem_imps = gasto + tarifa + ilum
        icms = (gasto * 0.25) 
        pis =  (gasto * 0.0375)
        total = gasto + ilum + icms + pis + bandeira 
        utils.clear()
        print(f""" ****** TALÃO MENSAL XPTO ******
Consumidor: {nome_consumidor}
Consumo: (KWh): {kwh}
consumo (R$): R$ {gasto:.2f} (valor por KWh:R$ {gastokwh})
Bandeira da Taifária: R$ {tarifa}
total sem imposto: {sem_imps:.2f}
ICMS: R$ {icms:.2f}
PIS/COFINS: {pis:.2f}
iluminação publica: R$ {ilum:.2f}
-------------------------------------------------------
Total a Pagar: R$ {total}
""")
        
main()