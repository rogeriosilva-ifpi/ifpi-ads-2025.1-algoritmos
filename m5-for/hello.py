def main():
  nome = input('Qual seu nome: ')
  qtd = int(input('Quantas vezes você quer ver seu nome: '))

  for i in range(0, qtd, 1):
    print(f'{i} >> Olá {nome}!')


main()