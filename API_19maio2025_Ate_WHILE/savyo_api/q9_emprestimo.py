def emprestimo():
    renda_mensal = float(input("Insira sua renda mensal: "))
    emprestimo = float(input("Insira o valor do emprestimo desejado: "))
    prazo = int(input("Insira a quantidade de parcelas desejadas: "))

    if prazo < 2 or prazo > 24:
        print("Parcelas inválidas")
        return
    if emprestimo < 1.518 :
        print("Impréstimo menor que o valor mínimo")
        return
    
    valor_maximo_parcela = renda_mensal * 0.30
    iof = (0.0038 * emprestimo) +  (0.000082 * emprestimo * prazo * 30)
    taxa = None

    if prazo <= 6:
        taxa = 0.1475 * 0.5
    elif prazo < 12:
        taxa = 0.1475 * 0.75
    elif prazo <= 18:
        taxa = 0.1475
    else:
        taxa = 0.1475 * 1.3
    
    juros = (emprestimo + iof) * taxa * prazo
    status = None
    valor_total = emprestimo + juros
    valor_mensal = valor_total / prazo

    if (valor_mensal < valor_maximo_parcela):
        status = "APROVADO"
    else:
        status = "REPROVADO"

    print(f"Valor do IOF : R${iof:.5f}")
    print(f"Juros a pagar: R${juros:.2f}")
    print(f"Valor total a pagar: R${valor_total:.2f}")
    print(f"Valor da parcela mensal: {prazo}x de R${valor_mensal:.2f}")
    print(f"O empréstimo foi {status}")

def main():
    emprestimo()

main()