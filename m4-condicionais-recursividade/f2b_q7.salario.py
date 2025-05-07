def main():
  salario = float(input('Salário R$: '))
  percentual = ''
  aumento = 0.0

  if salario <= 280:
    percentual = '20%'
    aumento = salario * (20/100)
  elif salario <= 700:
    percentual = '15%'
    aumento = salario * (15/100)
  elif salario <= 1.500:
    percentual = '10%'
    aumento = salario * (10/100)
  else:
    percentual = '5%'
    aumento = salario * (5/100)

  # saída
  novo_salario = salario + aumento
  resultado = f'''
  · o salário antes do reajuste: R$ {salario:.2f};
  · o percentual de aumento aplicado: {percentual};
  · o valor do aumento: R$ {aumento:.2f};
  · o novo salário, após o aumento: R$ {novo_salario:.2f}
  '''
  print(resultado)

main()