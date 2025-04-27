def main():
  numero = int(input('Número: '))

  somatorio = somar(numero)

  print('Somatório:', somatorio)


def somar(n):
  if n == 1:
    return 1
  
  return n + somar(n - 1)


main()