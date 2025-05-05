def main():
  n = int(input('N: '))

  somatorio = 0
  denominador = 1

  while denominador <= n:
    somatorio = somatorio + (1/denominador)
    denominador += 1
  
  print(f'S = {somatorio:.8f}')

main()