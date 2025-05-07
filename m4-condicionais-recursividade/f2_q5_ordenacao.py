def main():
  a = int(input('A: '))
  b = int(input('B: '))
  c = int(input('C: '))

  menor = None
  meio = None
  maior = None

  if a < b and a < c:
    menor = a
    if b < c:
      meio = b
      maior = c
    else:
      meio = c
      maior = b
  elif b < a and b < c:
    menor = b
    if a < c:
      meio = a
      maior = c
    else:
      meio = c
      maior = a
  else:
    menor = c
    if a < b:
      meio = a
      maior = b
    else:
      meio = b
      maior = a

  # resultado
  print('Ordenados: ', menor, meio, maior)

main()