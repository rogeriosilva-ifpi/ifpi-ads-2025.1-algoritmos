nome_consumidor = (input("Insira o nome do Consumidor: "))
Consumo_Kwh = int(input("Insira o Consumo Elétrico em KwH/mes: "))
bandeira = int(input("Escolha a tarifa da bandeira, se a bandeira for verde, coloque o preço como 0:"))
Gasto_Kwh = Consumo_Kwh * 0.89
tarifa_iluminação = ((Gasto_Kwh / 100) * 3)

def custo(Gasto_Kwh):
    if Gasto_Kwh <= 30:
        valor_processado = 0

    elif Gasto_Kwh <= 200:
        valor_processado = Consumo_Kwh + tarifa_iluminação
    
    elif Gasto_Kwh >= 200:
        valor_processado = (((Gasto_Kwh/100) * 30) + Gasto_Kwh) + tarifa_iluminação

    return(valor_processado)
 
icms = custo(Gasto_Kwh)/4
pins_cofins = (custo(Gasto_Kwh)/100) * 3.75

valorfinal = custo(Gasto_Kwh) + icms + pins_cofins 

print("TALÃO MENSAL XPTO "
        "Consumidor:", f'{nome_consumidor} '
        "Consumo(Kwh): ", f'{Consumo_Kwh} ' ,"Kwh/mês  "
        "Bandeira tarifária: ", f'{bandeira} '
        "Total sem impostos: ", f'{Gasto_Kwh:.2f}' ,"R$  "
        "ICMS:", f'{icms:.2f}' ,"R$  "
        "PIS/COFINS:", f'{pins_cofins:.2f}' ,"R$  "
        "Iluminação pública:", f'{tarifa_iluminação:.2f}' ,"R$  "
        "Total a pagar:", f'{valorfinal:.2f}') ,"R$  "

             



    

