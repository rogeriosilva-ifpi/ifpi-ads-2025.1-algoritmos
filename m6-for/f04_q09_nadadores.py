def main():
  pontos_a = 0
  pontos_b = 0
  prova = int(input('Prova: '))
  qtd_nadadores = int(input('Nadadores: '))

  while prova != 0 or qtd_nadadores != 0:
    for i in range(1, qtd_nadadores+1, 1):
      nome = input(f'Nome do Nadador {i}: ')
      classificacao = int(input(f'Classificação do {nome}: '))
      tempo = float(input('Tempo (s): '))
      clube = input('Clube (a, b): ')

      pontos = calcular_pontos(classificacao)

      if clube == 'a':
        pontos_a += pontos
      else:
        pontos_b += pontos


    prova = int(input('Prova: '))
    qtd_nadadores = int(input('Nadadores: '))
  
  # Computar resultado
  vencedor = 'Empate'
  if pontos_a > pontos_b:
    vencedor = 'Clube A venceu'
  elif pontos_b > pontos_a:
    vencedor = 'Clube B venceu'

  
  resultado = f'''
  Campeonato de Natação do CE
  Pontos Clube A: {pontos_a}
  Pontos Clube B: {pontos_b}
  Resultado: {vencedor}
  '''
  print(resultado)

  print('fim.')


def calcular_pontos(c: int) -> int:
  if c == 1:
    return 9
  elif c == 2:
    return 6
  elif c == 3:
    return 4
  elif c == 4:
    return 3
  else:
    return 0


main()