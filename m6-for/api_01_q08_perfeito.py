
def main():
  n = int(input('N: '))
  m = int(input('M: '))

  for numero in range(n, m+1, 1):
    resultado = perfeito(numero)
    print('>', numero, resultado)
  

  print('fim.')


def perfeito(numero):
  if somar_divisores(numero) == numero:
    return 'PERFEITO'
  else:
    return 'NÃO É PERFEITO'


def somar_divisores(numero):
  somatorio = 0
  for d in range(1, numero//2 + 1, 1):
    if numero % d == 0:
      somatorio += d
  
  return somatorio

main()