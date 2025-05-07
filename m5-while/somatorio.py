def main():
  qtd = int(input())
  somatorio = 0
  total = qtd
  

  while qtd > 0:
    somatorio = somatorio + int(input())
    qtd -= 1
  
  print(f'O somatório dos {total} números é {somatorio}')

main()