def main():
  n = int(input("N: "))
  limite_inf = get_integer_number_min("Limite Inferior: ", 0)
  limite_sup = get_integer_number_min('Limite Superior: ', limite_inf+1)
  
  escrever_multiplos(n, limite_inf, limite_sup)
  
  print('Fim.')


def escrever_multiplos(n, limite_inf, limite_sup):
  candidato = limite_inf
  
  while candidato <= limite_sup:
    if candidato % n == 0:
      print(candidato)

    candidato += 1

  
def get_integer_number(label):
  entrada = input(label)

  try:
    numero_a = int(entrada)
    return numero_a
  except ValueError:
    print('Valor Inteiro Inválido! ')
    return get_integer_number(label)


def get_integer_number_min(label, min_value):
  numero = get_integer_number(label)

  while numero < min_value:
    print(f'Valor deve ser no mínimo {min_value}')
    numero = get_integer_number(label)
  
  return numero

main()   




