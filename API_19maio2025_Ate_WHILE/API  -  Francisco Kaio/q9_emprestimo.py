def calcular_iof(valor, dias):
    return 0.0038 * valor + 0.00082 * valor * dias

def calcular_juros(valor, taxa_ano, meses):
    taxa_mes = taxa_ano / 12 / 100
    return valor + taxa_mes * meses

def simular_emprestimo():
    renda = float(input("Digite sua renda mensal: "))
    valor = float(input("Digite o valor desejado de empréstimo: "))
    parcelas = int(input("Quantas parecelas desejas (Min:2, Max:24): "))
    
    if parcelas < 2 or parcelas > 24:
        print ("Número de parcelas inválidos")
        
    elif valor < 1518:
        print ("Valor abaixo nop minimo permitido")
        
    elif valor > renda * 0.3:
        print ("Valor ultrapassa os 30% permitido")
        
    taxa_selic = 14.75
    dias = parcelas * 30
    juros = calcular_juros(valor, taxa_selic, parcelas)
    iof = calcular_iof(valor, dias)
    total = valor + juros + iof
    parcela = total / parcelas
    
    print (f"Valor do IOF: R$ {iof:.2f}")
    print (f"Juros a pagar: R$ {juros:.2f}")
    print (f"Valor total a pagar: R$ {total:.2f}")
    print (f"Parcela mensal: {parcelas}x de R$ {parcela:.2f}")
    
    if parcela <= renda * 0.3:
        print ("Empréstimo APROVADO")
    else:
        print ("Empréstimo NEGADO")
        
simular_emprestimo()