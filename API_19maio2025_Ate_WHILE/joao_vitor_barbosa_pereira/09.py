def main():
    iof = 0
    selic = 0.1475
    renda = pedirNumInt4()
    formaPagamento = """
Forma de pagamento
0 => a vista
1 => parcelado
"""
    print(formaPagamento)
    tipoPagamento = pedirNumInt("a forma de pagamento")
    emprestimo = pedirNumInt2("o valor do emprestimo")

    if tipoPagamento == 0:
        valorMaxParcela = renda * (30 / 100)
        iof += emprestimo * (0.0038)
        pagar = iof + emprestimo
        if pagar > valorMaxParcela:
            print("o valor final do seu emprestimo ultrapassa o limite de 30 por cento da sua renda.")
        else:
            print("o emprestimo foi bem sucedido!")
    else:
        valorMaxParcela = renda * (30 / 100)
        parcelas = pedirNumInt3("o número de parcelas")
        iof = emprestimo * (0.0038 + 0.000082 * (parcelas * 30))
        pagar = iof + emprestimo

        if parcelas <= 6:
            valorA = (pagar*(selic*(50/100)))
            pagar += valorA
        elif parcelas <= 6:
            valorA = (pagar*(selic*(75/100)))
            pagar += valorA
        elif parcelas <= 6:
            valorA = (pagar*(selic*(100/100)))
            pagar += valorA
        else:
            valorA = (pagar*(selic*(130/100)))
            pagar += valorA

        if (pagar/parcelas) > valorMaxParcela:
            print("o valor do seu emprestimo ultrapassa o limite de 30 por cento da sua renda.")
        else:
            resultado = f"""
o valor do IOF => {iof}
o valor do juros a pagar => {valorA}
o valor total a pagar => {pagar}
valor da parcela mensal => {pagar/parcelas}
"""
            print("o emprestimo foi bem sucedido!")

def pedirNumInt(referencia):
    try:
        value = int(input(f"Escreva {referencia}: "))
        if value == 0 or value == 1:
            return value
        else:
            print("valor invalido")
            return pedirNumInt(referencia)
    except ValueError:
        print("tente novamente")
        return pedirNumInt(referencia)

def pedirNumInt2(referencia):
    try:
        print("O valor minimo de empretimo é 1518")
        value = float(input(f"Escreva {referencia}: "))
        if value >= 1518:
            return value
        else:
            print("valor invalido")
            return pedirNumInt2(referencia)
    except ValueError:
        print("tente novamente")
        return pedirNumInt2(referencia)

def pedirNumInt3(referencia):
    try:
        print("Sua parcela deve estar no intevalo de 2 a 24")
        value = float(input(f"Escreva {referencia}: "))
        if value >= 2 and value <= 24:
            return value
        else:
            print("valor invalido")
            return pedirNumInt3(referencia)
    except ValueError:
        print("tente novamente")
        return pedirNumInt3(referencia)

def pedirNumInt4():
    try:
        value = int(input(f"Escreva o valor da renda: "))
        return value
    except ValueError:
        print("tente novamente")
        return pedirNumInt4()

main()