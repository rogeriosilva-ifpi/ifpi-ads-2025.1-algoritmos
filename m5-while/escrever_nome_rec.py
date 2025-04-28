def main():
  escrever_nome_n_vezes('Rogério Silva', 10)


def escrever_nome_n_vezes(nome, vezes):
  if vezes == 0:
    return

  print(vezes, nome)
  escrever_nome_n_vezes(nome, vezes - 1)


main()