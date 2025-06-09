def main():
  

  menu = '''
  >>>> WordPLAY <<<<
  1 - Palavras com Tamanho N+
  2 - Palavras sem Caracter Proibido

  0 - Sair
  >>>> '''

  option = int(input(menu))

  while option != 0:
    if option == 1:
      show_words_by_size()
    elif option == 2:
      show_words_without_forbidden_char()

    input('>>> continue...')
    option = int(input(menu))

  print('Fim.')


def show_words_by_size():
  size = int(input('Qual tamanho min das palavras: '))
  file = open('br-sem-acentos.txt')
  counter = 0
  filter_counter = 0
  for line in file:
    word = line.strip()
    counter += 1
    if len(word) >= size:
      filter_counter += 1
      print(word)
  
  print('------------')
  percentage = filter_counter / counter * 100
  print(f'Total/Filtro: {filter_counter}/{counter} ({percentage:.3f}%)')


def show_words_without_forbidden_char():
  file = open('br-sem-acentos.txt')
  forbidden = input('Qual é a letra proibida? ')
  counter = 0
  filter_counter = 0

  for line in file:
    word = line.strip()
    counter += 1
    if has_no_char_x(word, forbidden):
      filter_counter += 1
      print(word)

  print('------------')
  percentage = filter_counter / counter * 100
  print(f'Total/Filtro: {filter_counter}/{counter} ({percentage:.3f}%)')



def has_no_char_x(word, forbidden_char):
  for char in word:
    if char == forbidden_char:
      return False
  
  return True


main()