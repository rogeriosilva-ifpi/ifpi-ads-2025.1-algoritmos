# Questão 10)

def tarifas():
    consumidor = input('Informe o nome do consumidor: ')
    consumo_kwh = int(input('Informa o consumo do em KWh/mês: '))
    
    if consumo_kwh <= 30:
        valor_kwh_ate_30 = 0.0
        valor_consumo_ate30 = consumo_kwh * valor_kwh_ate_30
        tarifa_iluminacao = 0.03 * valor_consumo_ate30
        valor_sem_impostos_ate30 = valor_consumo_ate30
        calculo_icms = 0.25 * valor_sem_impostos_ate30
        calculo_pis_confins = 0.0375 * valor_sem_impostos_ate30
        
        total_a_pagar = valor_sem_impostos_ate30 + calculo_icms + calculo_pis_confins + tarifa_iluminacao
        
        print(f'''
****** TALÃO MENSAL XPTO ******          
Consumidor: {consumidor}
Consumo (KWh): {consumo_kwh}
Consumo (R$): R${valor_consumo_ate30:.2f} (valor por KWh: R${valor_kwh_ate_30:.2f}) 
Total sem impostos: R${valor_sem_impostos_ate30:.2f}
ICMS: R${calculo_icms:.2f}
PIS/CONFINS: R${calculo_pis_confins:.2f}
Iluminação pública: R${tarifa_iluminacao:.2f}
------------------------------------
Total a pagar: R${total_a_pagar:.2f}''')

    
    elif 30 < consumo_kwh <= 100:
        valor_kwh_padrao = 0.89
        valor_consumo_30_100 = consumo_kwh * valor_kwh_padrao
        tarifa_iluminacao = 0.03 * valor_consumo_30_100
        valor_sem_impostos_30_100 = valor_consumo_30_100
        calculo_icms = 0.25 * valor_sem_impostos_30_100
        calculo_pis_confins = 0.0375 * valor_sem_impostos_30_100
        
        total_a_pagar = valor_sem_impostos_30_100 + calculo_icms + calculo_pis_confins + tarifa_iluminacao
        print(f'''
****** TALÃO MENSAL XPTO ******          
Consumidor: {consumidor}
Consumo (KWh): {consumo_kwh}
Consumo (R$): R${valor_consumo_30_100:.2f} (valor por KWh: R${valor_kwh_padrao:.2f})
Total sem impostos: R${valor_sem_impostos_30_100:.2f}
ICMS: R${calculo_icms:.2f}
PIS/CONFINS: R${calculo_pis_confins:.2f}
Iluminação pública: R${tarifa_iluminacao:.2f}
------------------------------------
Total a pagar: R${total_a_pagar}''')

    
    elif consumo_kwh >= 200:
        valor_kwh_acima200 = 0.89 * 1.30
        valor_consumo_mais200 = consumo_kwh * valor_kwh_acima200
        tarifa_iluminacao = 0.03 * valor_consumo_mais200
        valor_sem_impostos_mais200 = valor_consumo_mais200
        calculo_icms = 0.25 * valor_sem_impostos_mais200
        calculo_pis_confins = 0.0375 * valor_sem_impostos_mais200
        
        total_a_pagar = valor_sem_impostos_mais200 + calculo_icms + calculo_pis_confins + tarifa_iluminacao
        print(f'''
****** TALÃO MENSAL XPTO ******          
Consumidor: {consumidor}
Consumo (KWh): {consumo_kwh}
Consumo (R$): R${valor_sem_impostos_mais200:.2f} (valor por KWh: R${valor_kwh_acima200:.2f}) 
Total sem impostos: R${valor_sem_impostos_mais200:.2f}
ICMS: R${calculo_icms:.2f}
PIS/CONFINS: R${calculo_pis_confins:.2f}
Iluminação pública: R${tarifa_iluminacao:.2f}
------------------------------------
Total a pagar: R${total_a_pagar:.2f}''')


executar_tarifas = tarifas()