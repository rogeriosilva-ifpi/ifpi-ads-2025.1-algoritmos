
from utilidades import calcular_percentual, parcelamento


def principal():
  valor_compra = float(input('Valor da Compra (R$): '))
  perc_desconto = float(input('Desconto (%): '))
  qtd_parcelas = int(input('Qtd Parcelas: '))

  valor_desconto = calcular_percentual(valor_compra, perc_desconto)
  valor_pagar = valor_compra - valor_desconto
  valor_parcela = parcelamento(valor_pagar, qtd_parcelas)

  resultado = f"""
  Valor da Compra: R$ {valor_compra:.2f}
  Desconto: -R$ {valor_desconto:.2f} ({perc_desconto:.1f}%)
  Valor a Pagar: R$ {valor_pagar:.2f} 
  Parcelas {qtd_parcelas}x de R$ {valor_parcela:.2f}
  """
  
  print(resultado)


principal()