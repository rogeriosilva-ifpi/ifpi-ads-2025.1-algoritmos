
from io_utils import obter_numero_inteiro, obter_numero_inteiro_min


def main():
  # ano = obter_numero_inteiro('Ano: ')
  ano = obter_numero_inteiro_min('Ano: ', 1000)

  if eh_bissexto(ano):
    print(f'O ano {ano} é bissexto!')
  else:
    print(f'O ano {ano} NÃO é bissexto!')


def eh_bissexto(ano: int):
  return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

main()