def main():
  print('Início')
  conta = obter_decimal('Valor da Conta R$: ')
  pagantes = obter_inteiro('Pagantes: ')

  try:
    valor_individual = conta / pagantes
    print(f'Cada um pagará R$ {valor_individual:.2f}')
  except ZeroDivisionError:
    print('Não é possível processar a conta sem Pagantes!')

  print('Fim.')


def obter_decimal(texto):
  try:
    return float(input(texto))
  except ValueError:
    print('Bora tentar novamente!!!')
    return obter_decimal(texto)
  

def obter_inteiro(texto):
  numero = input(texto)
  try:
    return int(numero)
  except:
    print(f'O valor "{numero}" não é válido!')
    return obter_inteiro('*'+texto)


main()
