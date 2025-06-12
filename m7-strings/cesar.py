import time

def main():
  texto = input('Texto: ')
  chave = int(input('Chave: '))

  criptografado = cesar_cripto(texto, chave)

  print(criptografado)


def cesar_cripto(texto, chave):
  novo_texto = ''

  for caracter in texto:
    novo_texto += deslocar_caracter_ascii(caracter, chave)
  
  return novo_texto

def deslocar_caracter_ascii(caracter, chave):
  novo_codigo = ord(caracter) + chave

  if novo_codigo > 126:
    novo_codigo = novo_codigo % 126
  elif novo_codigo < 32:
    novo_codigo = 126 - (novo_codigo % 32)

  return chr(novo_codigo)

  

start = time.time()
main()
duration = time.time() - start

print(f'Tempo: {duration:.7f}')