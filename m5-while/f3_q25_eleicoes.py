def main():
  eleitores = int(input('Qtd Eleitores: '))
  contador = 0
  votos_1 = 0
  votos_2 = 0
  votos_3 = 0
  nulos = 0
  brancos = 0

  while contador < eleitores:
    voto = obter_voto()

    if voto == 1: votos_1 += 1
    if voto == 2: votos_2 += 1
    if voto == 3: votos_3 += 1
    if voto == 9: nulos += 1
    if voto == 0: brancos += 1

    contador += 1
  vencedor = 'Empate'
  if votos_1 > votos_2 and votos_1 > votos_3:
    vencedor = 'Candidato 01'
  elif votos_2 > votos_1 and votos_2 > votos_3:
    vencedor = 'Candidato 02'
  elif votos_3 > votos_1 and votos_3 > votos_2:
    vencedor = 'Candidato 03'

  resultado = f'''
  ------ Resultado -------
  a) total de votos para cada candidato;
    Candidato 01: {votos_1} votos
    Candidato 02: {votos_2} votos
    Candidato 03: {votos_3} votos
  b) total de votos nulos;
    Nulos: {nulos}
  c) total de votos em branco;
    Brancos: {brancos}
  d) quem venceu a eleição.
    Resultado: {vencedor}
  '''

  print(resultado)


def obter_voto():
  urna = '''
  Opções:
  1 = Canditado 01
  2 = Canditado 02
  3 = Canditado 03
  0 = Branco
  9 = Nulo

  Qual seu voto >>>> '''

  voto = int(input(urna))
  return voto

main()