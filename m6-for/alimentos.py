alimentos = {
  'frango': 00,
  'carne': 88
 }

def obter_valor_valido():
  alimento = input()

  for chave in alimentos:
    if alimento == chave:
      return alimento
  
  return obter_valor_valido()

