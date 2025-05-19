RendaMensal = int(input("insira a sua renda mensal: "))
ValorEmprestimo = int(input("insira o valor do empréstimo: "))
prazo = int(input("insira o prazo em meses: ")) * 30
iof = (ValorEmprestimo/100 * 0.38) + ((ValorEmprestimo/100 * 0.0082) * prazo)
valortaxado = iof + ValorEmprestimo
parcelas = prazo/30
def juros(prazo, valortaxado):
    if (prazo / 30) <= 6:
        jurospagos = ((valortaxado/100) *  7.375 )
        print(f"o valor dos juros será de:", jurospagos, "reais")
        

    elif (prazo / 30) <= 12:
        jurospagos = ((valortaxado/100) *  11.0625 )
        print(f"o valor dos juros será de:", jurospagos, "reais")
    
    elif (prazo / 30) <= 17:
        jurospagos = ((valortaxado/100) *  14.75 )
        print(f"o valor dos juros será de:", jurospagos, "reais")

    elif (prazo / 30) == 18:
        jurospagos = ((valortaxado/100) *  14.75 )
        print(f"o valor dos juros será de:", jurospagos, "reais")

    elif (prazo / 30) >= 18:
        jurospagos = ((valortaxado/100) *  19.175 )
        print(f"o valor dos juros será de:", jurospagos, "reais")
    
    return(jurospagos)

valortotal = juros(prazo,valortaxado) + valortaxado
parcelamento = valortotal/parcelas

def aprovar(RendaMensal, parcelamento):
    if RendaMensal > parcelamento:
        print("O empréstimo está APROVADO")

    else:
        print("O empréstimo está NEGADO")


juros(prazo, valortaxado)

print (f"O valor do Imposto Sobre operações financeiras será de", iof, "Reais")
print (f"O valor total a pagar é: ", f'{valortotal:.2f}', "reais")
print (f"O valor da parcela mensal será de ",f'{parcelas}',"x de", f'{parcelamento:.2f}', "reais")
aprovar(RendaMensal, parcelamento)
