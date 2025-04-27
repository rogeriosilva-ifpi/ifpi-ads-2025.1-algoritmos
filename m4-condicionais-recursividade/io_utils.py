# IO --> Input/Output functions

def obter_numero_real(label: str):
  return float(input(label))

def obter_numero_inteiro(label: str):
  entrada = input(label)
  try:
    numero = int(entrada)
    return numero
  except ValueError:
    print(f'O valor "{entrada}" não é um inteiro válido!')
    return obter_numero_inteiro(label)
  

def obter_numero_inteiro_min(label: str, min: int):
  numero = obter_numero_inteiro(label)

  if numero >= min:
    return numero
  else:
    print(f'O número deve ser no mínimo {min}')
    return obter_numero_inteiro_min(label, min)
  