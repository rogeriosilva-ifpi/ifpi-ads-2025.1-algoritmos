def main():
  

  menu = '''
  >>>> WordPLAY <<<<
  1 - Palavras com Tamanho N+

  0 - Sair
  >>>> '''

  opcao = int(input(menu))

  while opcao != 0:
    if opcao == 1:
      mostrar_palavras_por_tamanho()
    input('>>> continue...')
    opcao = int(input(menu))

  print('Fim.')\
  

def mostrar_palavras_por_tamanho():
  tamanho = int(input('Qual tamanho min das palavras: '))
  arquivo = open('br-sem-acentos.txt')
  contador = 0
  contador_filtro = 0
  for linha in arquivo:
    palavra = linha.strip()
    contador += 1
    if len(palavra) >= tamanho:
      contador_filtro += 1
      print(palavra)
  
  print('------------')
  percentual = contador_filtro / contador * 100
  print(f'Total/Filtro: {contador_filtro}/{contador} ({percentual:.1f}%)')


main()