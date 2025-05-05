def main():
  n = int(input('N: '))
  somatorio = 0
  numerador = 1
  denominador = n

  while numerador <= n:
    somatorio += numerador / denominador
    numerador += 1
    denominador -= 1
  
  print(f'S = {somatorio:.6}')


main()