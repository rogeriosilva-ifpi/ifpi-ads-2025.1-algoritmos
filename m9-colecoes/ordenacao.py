import random

from tkinter.tix import Tree

def main():
  numeros = gerar_lista(10)
  print(numeros)
  
  r = numeros.sort()
  # print(r)
  # ordenacao padrão
  numeros_ord = sorted(numeros)

  # botar em ordem decrescente
  numeros.sort(reverse=True)
  numeros_ord = sorted(numeros, reverse=True)
  print(numeros_ord)



def gerar_lista(qtd):
  lista = []
  for _ in range(qtd):
    lista.append(random.randint(1, 100))

  return lista
main()