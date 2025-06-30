
def main():
  # packing and unpacking
  valores = mapear(input().split(), int)

  valores_positivos = filtrar(valores, eh_positivo)
  valores_negativos = filtrar(valores, eh_negativo)

  somatorio_positivos = reduzir(valores_positivos, somar, 0)
  somatorio_negativos = reduzir(valores_negativos, somar, 0)

  print('Valores Positivos: ', valores_positivos)
  print('Somatório Positivos: ', somatorio_positivos)

  print('Valores Negativos: ', valores_negativos)
  print('Somatório Negativos: ', somatorio_negativos)

  print('A Soma dos Pares', reduzir(filtrar(valores, eh_par_nao_nulo), multiplicar, 1))
  print('O maior valor de todos é', reduzir(valores, maior, valores[0]))


def maior(valor1, valor2):
  # if valor1 > valor2:
  #   return valor1

  # return valor2
  return valor1 if valor1 > valor2 else valor2

def mapear(colecao, funcao_transformadora):
  nova_colecao = []

  for item in colecao:
    item_transformado = funcao_transformadora(item)
    nova_colecao.append(item_transformado)
  
  return nova_colecao


def eh_positivo(valor):
  return valor > 0


def eh_negativo(valor):
  return valor < 0


def eh_par_nao_nulo(valor):
  return valor != 0 and valor % 2 == 0


def multiplicar(valor1, valor2):
  return valor1 * valor2


def somar(valor1, valor2):
  return valor1 + valor2


def filtrar(colecao, criterio):
  nova_colecao = []

  for item in colecao:
    if criterio(item):
      nova_colecao.append(item)

  return nova_colecao


def reduzir(colecao, redutora, inicial):
  acumulado = inicial

  for item in colecao:
    acumulado = redutora(acumulado, item)

  return acumulado


if __name__ == '__main__':
  main()