def main():
  qtd = int(input())

  while qtd > 0:
    numero = int(input())
    sobrenome = 'EVEN' if numero % 2 == 0 else 'ODD'

    if numero > 0:
      print(f'{sobrenome} POSITIVE')
    elif numero < 0:
      print(f'{sobrenome} NEGATIVE') 
    else:
      print('NULL')

    qtd -= 1


main()