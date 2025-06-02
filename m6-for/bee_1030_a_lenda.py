def lenda():
  casos = int(input('Casos: '))

  for i in range(1, casos + 1, 1):
    entrada = input(f'Caso {i}: ')
    pessoas = int(entrada.split()[0])
    k = int(entrada.split()[1])

    lista = list(range(1, pessoas + 1, 1))
    pos_atual = k - 1
    saltos = k
    
    while contar_vivos(lista) > 1:
      if saltos == k:
        lista[pos_atual] = 0
        saltos = 0

      pos_atual += 1
      if pos_atual >= len(lista):
        pos_atual = 0
      
      while lista[pos_atual] == 0:
        pos_atual += 1
        if pos_atual >= len(lista):
          pos_atual = 0
      
      saltos += 1

  mostrar_vivo(lista)


def contar_vivos(lista):
  contador = 0
  for item in lista:
    if item != 0:
      contador += 1
  
  return contador


def mostrar_vivo(lista):
  if contar_vivos(lista) > 1:
    print('Há mais de um vivo na lista')
    return
  
  for item in lista:
    if item != 0:
      print(item)
      return


lenda()