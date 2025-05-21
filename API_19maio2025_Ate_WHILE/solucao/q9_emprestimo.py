from q2_int_utils import obter_inteiro_faixa, obter_inteiro_minimo, obter_inteiro_positivo


def main():
  valor = float(obter_inteiro_minimo('Valor Empréstimo(R$): ', 1518))
  qtd_parcelas = obter_inteiro_faixa('Qtd Parcelas: ', 2, 24)
  renda = float(obter_inteiro_positivo('Renda (R$): '))

  iof = calcular_iof(valor, qtd_parcelas)

  capital = valor + iof

  taxa = calcular_taxa(qtd_parcelas)

  juros = juros_simples(capital, qtd_parcelas, taxa)

  montante = capital + juros

  valor_parcela = montante / qtd_parcelas

  parcela_maxima = renda * 30/100

  situacao = 'APROVADO' if valor_parcela <= parcela_maxima else 'NEGADO'

  resultado = f'''
  a. Valor do IOF: R$ {iof:.2f}
  b. Valor dos Juros a pagar: R$ {juros:.2f}
  c. Valor Total a pagar: R$ {montante:.2f}
  d. Valor da Parcela Mensal: {qtd_parcelas}x de R$ {valor_parcela})
  e. Sua Parcela Máxima: R$ {parcela_maxima:.2f}
  \t Seu Empréstimo foi {situacao}.
  '''

  print(resultado)


def calcular_iof(valor, qtd_parcelas):
  iof = 0.38/100 * valor
  dias = qtd_parcelas * 30
  
  iof = iof + 0.0082/100 * valor * dias

  return iof


def calcular_taxa(qtd_parcelas):
  SELIC = 14.75/100
  if qtd_parcelas <= 6:
    return 50/100 * SELIC
  elif qtd_parcelas <= 12:
    return 75/100 * SELIC
  elif qtd_parcelas <= 18:
    return 100/100 * SELIC
  else:
    return 130/100 * SELIC
  

def juros_simples(capital, qtd_parcelas, taxa):
  juros = capital * taxa * qtd_parcelas
  return juros


main()