import os
from str_utils import avoids, is_abecedarian, to_lower, uses_all, uses_only

def main():
  

  menu = '''
  |>>>> WordPLAY <<<<|
  1 - Palavras com Tamanho N+ (9.1)
  2 - Palavras sem Caracter Proibido (9.2)
  3 - Palavras sem Letras Proibidas (9.3)
  4 - Palavras somente com Letras Permitidas (9.4)
  5 - Palavras com Letras Obrigatórias (9.5)
  6 - Palavras com Letras em Ordem Alfabética (9.6)

  0 - Sair
  >>>> '''

  option = int(input(menu))

  while option != 0:
    if option == 1:
      show_words_by_size()
    elif option == 2:
      show_words_without_forbidden_char()
    elif option == 3:
      forbidden_letters = input('Letras Proibidas: ')
      show_words_without_forbidden_letters(forbidden_letters)
    elif option == 4:
      allowed_letter = input('Letras Permitidas: ')
      show_words_without_allowed_letter(allowed_letter)
    elif option == 5:
      mandatory_letters = input('Letras Obrigatórios: ')
      show_words_with_mandatory_letters(mandatory_letters)
    elif option == 6:
      show_abecedarian_words()
      


    input('>>> continue...')
    clear_screen()
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


def show_words_without_forbidden_letters(forbidden_letters):
  file = open('br-sem-acentos.txt')

  for line in file:
    word = line.strip()
    if avoids(word, forbidden_letters):
      print(word)

def show_words_with_allowed_letters():
  sin = open("br-sem-acentos.txt")

def clear_screen():
  os.system('clear')


def show_words_without_allowed_letter(allowed_letters):
  file = open('br-sem-acentos.txt')
  counter = 0
  filter_counter = 0

  for line in file:
    word = line.strip()
    counter += 1
    if uses_only(word, allowed_letters):
      print(word)
      filter_counter += 1

  footer(counter, filter_counter)

def show_words_with_mandatory_letters(mandatory_letters):
  file = open('br-sem-acentos.txt')
  counter = 0
  filter_counter = 0

  for line in file:
    word = line.strip()
    counter += 1
    if uses_all(word, mandatory_letters):
      print(word)
      filter_counter += 1
  
  footer(counter, filter_counter)


def show_abecedarian_words():
  file = open('br-sem-acentos.txt')
  counter = 0
  filter_counter = 0

  for line in file:
    word = to_lower(line.strip())
    counter += 1
    if is_abecedarian(word):
      filter_counter += 1
      print(word)

  footer(counter, filter_counter)


def footer(counter, filter_counter):
  print('------------')
  percentage = filter_counter / counter * 100
  print(f'Total/Filtro: {filter_counter}/{counter} ({percentage:.3f}%)')
  

main()