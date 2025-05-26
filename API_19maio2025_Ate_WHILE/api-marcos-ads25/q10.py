def calcular_talão(nome, consumo):
    valor_kwh = 0.89

    if consumo <= 30:
        print('----------TALÃO MENSAL XPTO----------')
        print(f'CONSUMIDOR: {nome}')
        print(f'CONSUMO(KWh): {consumo}')   
        print(f'CONSUMO(R$): R$0 (valor por KWh: R$ 0)')
        print(f'Bandeira Tarifaria: R$0')
        print(f'Total sem imposto: R$0')
        print(f'ICMS: 0')
        print(f'PIS/CONFINS: 0')
        print(f'Iluminacao publica: R$0')
        print(f'-------------------------------------')
        print(f'TOTAL A PAGAR :  R$ 0')
        return
    if consumo > 30 and consumo <= 200:
        valor_tarifa= consumo*0.89
        tarifa_iluminacao = 0.03*valor_tarifa
        valor_parcial = valor_tarifa + tarifa_iluminacao

        icms = valor_parcial*0.25 
        pis = valor_parcial*0.0375

        valor_total = valor_parcial + icms + pis

        print('----------TALÃO MENSAL XPTO----------')
        print(f'CONSUMIDOR: {nome}')
        print(f'CONSUMO(KWh): {consumo}')   
        print(f'CONSUMO(R$): R${valor_tarifa} (valor por KWh: R$ {valor_kwh})')
        print(f'Bandeira Tarifaria: R$0')
        print(f'Total sem imposto: R${valor_parcial}')
        print(f'ICMS:{icms}')
        print(f'PIS/CONFINS: {pis}')
        print(f'Iluminacao publica: R${tarifa_iluminacao}')
        print(f'-------------------------------------')
        print(f'TOTAL A PAGAR :  R$ {valor_total}')
        return
    if consumo > 200:
        valor_200_mais = 0.89 *1.3
        valor_tarifa= consumo*valor_200_mais
        tarifa_iluminacao = 0.03*valor_tarifa
        valor_parcial = valor_tarifa + tarifa_iluminacao

        icms = valor_parcial*0.25 
        pis = valor_parcial*0.0375

        valor_total = valor_parcial + icms + pis

        print('----------TALÃO MENSAL XPTO----------')
        print(f'CONSUMIDOR: {nome}')
        print(f'CONSUMO(KWh): {consumo}')   
        print(f'CONSUMO(R$): R${valor_tarifa} (valor por KWh: R$ {valor_200_mais})')
        print(f'Bandeira Tarifaria: R$0')
        print(f'Total sem imposto: R${valor_parcial}')
        print(f'ICMS:{icms}')
        print(f'PIS/CONFINS: {pis}')
        print(f'Iluminacao publica: R${tarifa_iluminacao}')
        print(f'-------------------------------------')
        print(f'TOTAL A PAGAR :  R$ {valor_total}')
        return

def main():

    n = int(input('De quantas familias deseja extrair o talão de energia? '))
    i = 1 

    while i <= n :
        print(f'------------Familia {i}------------')

        nome = input('Digite o nome do responsavel: ')
        consumo = int(input('Digite o consumo da casa: '))
        
        calcular_talão(nome,consumo)
        i+=1

main()