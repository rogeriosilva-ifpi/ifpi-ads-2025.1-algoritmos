
consumidor = input("Digite o nome do consumidor: ").upper()
consumo_de_energia = float(input("Digite de quantos KWh foi o seu consumo este mês: "))

valor_padrao_do_kwh = 0.89
fatura_padrao = consumo_de_energia * valor_padrao_do_kwh

def verifica_isencao_ou_adicional(consumo_de_energia, fatura_padrao):
    if consumo_de_energia <= 30:
        return verificar_isencão()
    elif consumo_de_energia > 200:
        return verificar_custo_adicional(fatura_padrao)
    else:
        custo_padrao()

def verificar_isencão():
    valor_da_conta = 0
    float(valor_da_conta)
    mensagem = f"Consumo(R$): {valor_da_conta :.2f}"
    return print(mensagem)


def verificar_custo_adicional(fatura_padrao):
    custo_adicional = fatura_padrao * 0.3
    nova_fatura = fatura_padrao + custo_adicional
    mensagem = f"Consumo(R$): {nova_fatura :.2f}"
    return print(mensagem)

def custo_padrao():
    float(fatura_padrao)
    mensagem = f"Consumo(R$): {fatura_padrao :.2f}"
    return print(mensagem)

def tarifa_de_iluminacao(fatura_padrao):
    tarifa = fatura_padrao * 0.03
    mensagem = f"Iluminação Pública: R$ {tarifa:.2f}"
    return print(mensagem)

def calcular_pis_cofins(fatura_padrao):
    pis_cofins = fatura_padrao * 0.0375
    mensagem = f"PIS/COFINS: R$ {pis_cofins :.2f}"
    return print(mensagem)

def calcular_icms(fatura_padrao):
    icms = fatura_padrao * 0.25
    mensagem = f"ICMS: R$ {icms :.2f}"
    return print(mensagem)

def total(fatura_padrao):
    valor_1 = verifica_isencao_ou_adicional(consumo_de_energia, fatura_padrao)
    valor_2 = calcular_icms(fatura_padrao)
    valor_3 = calcular_pis_cofins(fatura_padrao)
    valor_4 = tarifa_de_iluminacao(fatura_padrao)
    soma = valor_1 + valor_2 + valor_3 + valor_4
    mensagem = f"{soma}"
    return print(mensagem)

def consumidor_formatado(consumidor):
    mensagem = f"Consumidor: {consumidor}"
    return print(mensagem)

def consumo_formatado(consumo_de_energia):
    mensagem = f"Consumo (KWh): {consumo_de_energia :.2f} (valor por KWh: R$ 0,89)"
    return print(mensagem)

print("*" *5,"TALÃO MENSAL XPTO", "*" *5)
consumidor_formatado(consumidor)
consumo_formatado(consumo_de_energia)
print(f"Total sem impostos: ", fatura_padrao)
verifica_isencao_ou_adicional(consumo_de_energia, fatura_padrao)
calcular_icms(fatura_padrao)
calcular_pis_cofins(fatura_padrao)
tarifa_de_iluminacao(fatura_padrao)
total(fatura_padrao)


