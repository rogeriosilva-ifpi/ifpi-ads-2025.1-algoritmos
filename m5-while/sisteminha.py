import os


def main():
  somatorio = 0
  contador = 0
  clear_screen()

  while True:
    show_menu()
    opcao = int(input('Digite sua opção >>> '))

    if opcao == NEW_NUMBER:
      somatorio = somatorio + int(input('Novo Número > '))
      contador += 1
    elif opcao == COUNT:
      print(f'Temos {contador} números cadastrados.')
    elif opcao == AVERAGE:
      media = somatorio / contador
      print(f'A Média dos {contador} números é {media:.1f}')
    elif opcao == EXIT:
      clear_screen()
      break
    elif opcao == SUM:
      print(f'A Soma dos {contador} números é {somatorio}')
    else:
      print('Opção inválida!')
      enter_to_continue()
      continue
    
    print('Operação realizada com sucesso!')
    enter_to_continue()


def enter_to_continue():
  input('<Enter> to continue...')
  clear_screen()

def clear_screen():
  os.system('clear')


def show_menu():
  menu = '''
  ======= SysNumbers ======
  1 - Adicionar novo número
  2 - Quantidade de números
  3 - Somatório dos números
  4 - Média dos números
  ...
  0 - Encerrar
  '''
  print(menu)

# Constantes
EXIT = 0
NEW_NUMBER = 1
SUM = 3
AVERAGE = 4
COUNT = 2


main()