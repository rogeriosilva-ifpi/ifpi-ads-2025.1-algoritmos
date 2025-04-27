def main():
  lado_a = int(input('lado A:'))
  lado_b = int(input('lado B:'))
  lado_c = int(input('lado C:'))

  if eh_triangulo(lado_a, lado_b, lado_c):
    print('Os lados formam um triangulo!')
    if eh_degenerado(lado_a, lado_b, lado_c):
      print('Entretanto, ele é um DEGENERADO!')
  else:
    print('Os lados NÃO formam um triângulo!')
  

  print('Fim por fim feito por mim!')


def eh_triangulo(a: int, b: int, c: int): 
  return a <= b + c and b <= a + c and c <= a + b


def eh_degenerado(a: int, b: int, c: int):
  return eh_triangulo(a, b, c) and (a == b + c or b == a + c or c == a + b)


main()