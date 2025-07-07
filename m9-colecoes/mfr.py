
def mapear(colecao, funcao_transformadora):
  nova_colecao = []

  for item in colecao:
    item_transformado = funcao_transformadora(item)
    nova_colecao.append(item_transformado)
  
  return nova_colecao


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

