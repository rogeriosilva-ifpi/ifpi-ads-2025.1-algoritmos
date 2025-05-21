def main():
  # n = obter_inteiro('N: ')
  # n = obter_inteiro_while('N: ')
  # n = obter_inteiro_positivo('N: ')
  # n = obter_inteiro_minimo('N: ', 100)
  # n = obter_inteiro_maximo('N: ', 100)
  n = obter_inteiro_faixa('N: ', 7, 10)
  print(f'Valor: {n}')


def obter_inteiro(label):
  valor = input(label)

  try:
    numero = int(valor)
    return numero
  except ValueError:
    print('Valor inválido!')
    return obter_inteiro(label)


def obter_inteiro_while(label):
  while True:
    try:
      numero = int(input(label))
      return numero
    except ValueError:
      print('Valor inválido!')


def obter_inteiro_positivo(label):
  numero = obter_inteiro(label)

  while numero <= 0:
    print('Valor inválido!')
    numero = obter_inteiro(label)

  return numero


def obter_inteiro_negativo(label):
  numero = obter_inteiro(label)

  while numero >= 0:
    print('Valor inválido!')
    numero = obter_inteiro(label)

  return numero


def obter_inteiro_minimo(label, x):
  numero = obter_inteiro(label)

  while numero < x:
    print('Valor inválido!')
    numero = obter_inteiro(label)

  return numero


def obter_inteiro_maximo(label, x):
  numero = obter_inteiro(label)

  while numero > x:
    print('Valor inválido!')
    numero = obter_inteiro(label)

  return numero


def obter_inteiro_faixa(label, minimo, maximo):
  

  while True:
    numero = obter_inteiro(label)
    if numero >= minimo and numero <= maximo:
      return numero
    
    print('Valor inválido!')
    
  return numero

if __name__ == '__main__':
  main()