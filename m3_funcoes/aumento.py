from utilidades import calcular_percentual

def principal():
  salario = float(input('Salário: '))
  percentual = float(input('Aumento (%): '))

  reajuste: float = calcular_percentual(salario, percentual)

  novo_salario: float = salario + reajuste

  print(f'Você terá um reajusts de {percentual}%')
  print(f'Seu salário vai passar de R$ {salario}')
  print(f'para R$ {novo_salario}. Ou seja, R$ {reajuste}({percentual}%) de aumento')



principal()