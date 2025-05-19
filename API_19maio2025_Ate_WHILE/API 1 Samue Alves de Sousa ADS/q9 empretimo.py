def emprestimo():
    
    renda_mensal = float(input('Digite seu salario: '))
    valor_emprestimo = float(input('Qual vai ser o valor do emprestimo? '))
    prazo = int(input('Qauntas vezes? DIGITAR SO QTD DE PARCELAS '))

    dias_emprestimo = prazo * 30
    base_iof = (valor_emprestimo) / 100 * 0.38 * dias_emprestimo
    iof = base_iof + (valor_emprestimo) * 0.0082

    if renda_mensal < 1518.00:
        print('Emprestimo NEGADO ):')
    elif prazo > 1 or prazo <= 6:
        selic = (valor_emprestimo) + 50/100 + iof
        print(f'O valor do empretimo com juros é de {selic}R$ \n divido em {prazo}X de {selic / prazo:.3f} !!!!')

    elif prazo >= 7 or prazo <= 12:
        selic = (valor_emprestimo) + 75/100 + iof
        print(f'O valor do empretimo com juros é de {selic}R$ \n divido em {prazo}X de {selic / prazo:.3f} !!!!')

    elif prazo >= 10 or prazo <= 18:
        selic = (valor_emprestimo) + 100/100 + iof
        print(f'O valor do empretimo com juros é de {selic}R$ \n divido em {prazo}X de {selic / prazo:.3f} !!!!')

    elif prazo > 18 and prazo <= 24:
        selic = (valor_emprestimo) + 130/100 + iof
        print(f'O valor do empretimo com juros é de {selic}R$ \n divido em {prazo:.3}X de {selic / prazo:.3f} !!!!')


emprestimo()     
