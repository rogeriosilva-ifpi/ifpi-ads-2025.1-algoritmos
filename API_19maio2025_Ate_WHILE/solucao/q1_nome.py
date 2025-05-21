def main():
  nome = input('Nome: ')
  tamanho = len(nome)
  print(f'O Nome tem {tamanho} caracteres.')

  if tamanho % 2 == 0: # par
    contador = 0
    atual = tamanho + tamanho
    while contador < tamanho:
      print(atual)
      atual = atual + tamanho
      contador += 1
  else: # impar
    candidato = tamanho

    while candidato > 0:
      if tamanho % candidato == 0:
        print(candidato)
      candidato -= 1



main()