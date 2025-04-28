def main():
  num1 = int(input('Número 1: '))
  num2 = int(input('Número 2: '))
  maior = num1 if num1 > num2 else num2
  mmc = maior

  while not (mmc % num1 == 0 and mmc % num2 == 0):
    print('*', end='')
    mmc = mmc + maior
  
  print(f'\nO MMC({num1}, {num2}) = {mmc}')


main()