def main():
  somatorio = 0
  contador = 0

  while True:
    try:
      numero = int(input())
    except EOFError:
      break
    except ValueError:
      continue

    if numero < 0:
      continue

    somatorio = somatorio + numero
    contador += 1
  
  print(f'A soma dos {contador} números é {somatorio}')


main()