from q2_int_utils import obter_inteiro_minimo, obter_inteiro_positivo


def main():
  n = obter_inteiro_positivo('N: ')
  m = obter_inteiro_minimo('M: ', n + 2)

  numero = n

  while numero <= m:
    if eh_primo(numero):
      print(f'O número {numero} é PRIMO!')
    
    numero += 1

  print('fim.')


def eh_primo(numero):
  # candidato = numero - 1
  candidato = int(numero**0.5)

  while candidato > 1:
    if numero % candidato == 0:
      return False
    
    candidato -= 1
  
  return True

main()