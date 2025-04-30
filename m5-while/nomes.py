def main():
  qtd = int(input('Qut de Nomes: '))
  contador_caractres = 0

  while qtd > 0:
    nome = input('Nome: ')
    contador_caractres += len(nome)
    qtd = qtd - 1
  

  print(f"Os nomes que vc digitou tem {contador_caractres} caracteres.")


main()