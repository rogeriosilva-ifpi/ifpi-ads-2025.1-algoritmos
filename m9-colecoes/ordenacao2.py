def main():
  nomes = ['Maria', 'Zoe', 'Ana', 'Joaquina', 'Pedro', 'Ti']
  print(nomes)
  # ordenados = sorted(nomes, key=len)
  ordenados = sorted(nomes, key=lambda p:p[len(p) - 1], reverse=True)
  print(ordenados)


main()