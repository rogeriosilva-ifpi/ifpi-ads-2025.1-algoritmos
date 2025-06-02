def lenda():
  casos = int(input())

  for i in range(1, casos + 1, 1):
    entrada = input()
    pessoas = int(entrada.split()[0])
    k = int(entrada.split()[1])

    lista = list(range(1, pessoas + 1, 1))
    pos_atual = k - 1
    saltos = k
    contador_vivos = pessoas
    
    while contador_vivos > 1:
      if saltos == k:
        lista[pos_atual] = 0
        saltos = 0
        contador_vivos -= 1

      pos_atual += 1
      if pos_atual >= len(lista):
        pos_atual = 0
      
      while lista[pos_atual] == 0:
        pos_atual += 1
        if pos_atual >= len(lista):
          pos_atual = 0
      
      saltos += 1

    mostrar_vivo(lista, i)


def mostrar_vivo(lista, case):
  for item in lista:
    if item != 0:
      print(f'Case {case}: {item}')
      return


lenda()