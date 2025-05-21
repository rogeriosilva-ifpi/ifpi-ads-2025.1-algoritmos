from q2_int_utils import obter_inteiro_positivo


def main():
  num1 = obter_inteiro_positivo('N1: ')
  num2 = obter_inteiro_positivo('N2: ')

  valor = mdc(num1, num2)

  print(f'>> MDC({num1}, {num2}) == {valor}')


def mdc(num1, num2):
  maior = 0
  menor = 0
  if num1 > num2:
    maior = num1
    menor = num2
  else:
    maior = num2
    menor = num1

  resto = maior % menor
  while resto != 0:
    maior = menor
    menor = resto

    resto = maior % menor

  return menor


main()