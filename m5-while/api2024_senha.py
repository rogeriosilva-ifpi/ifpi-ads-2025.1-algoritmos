import time
from random import randint


def main():
  print('----> GenPass <----')
  print('Olá vamos gerar um senha para você!')
  delay(600)
  
  tamanho = int(input('Tamanho: '))

  senha = gerar_senha(tamanho)

  print(f'Cá está sua senha: {senha}')
  delay(750)
  
  gostastes = int(input('Você gostou? 1 - Sim, 2 - Não: '))

  while gostastes != 1:
    print('Tudo bem! vou gerar um nova pra você.')
    delay(573)
    senha = gerar_senha(tamanho)
    print(f'Cá está sua senha: {senha}')
    delay(1000)
    gostastes = int(input('Você gostou? 1 - Sim, 2 - Não: '))
  
  print('Que bom que você gostou!')
  delay(764)
  print('Fim.')


def gerar_senha(tamanho: int):
  senha = ''
  anterior = ''
  while len(senha) < tamanho:
    atual = str(randint(0, 9))

    if anterior == '' or (atual != anterior and diferenca(atual, anterior) > 1):
      print('.', end='')
      anterior = atual
      senha = senha + atual
    else:
      delay(1000)
  print()
  
  return senha


def diferenca(valor1: str, valor2: str) -> int:
  a = int(valor1)
  b = int(valor2)

  diff = a - b

  if a >= b:
    return diff
  else:
    return -1 * diff



def delay(duration: int):
  time.sleep(duration/1000)


main()