import os


def main():
  limpar_tela()
  # contadores / ,,,
  qtd_aluno = 0
  qtd_aprovado = 0
  qtd_reprovado = 0
  qtd_provafinal = 0
  maior_media = -1
  menor_media = 11
  matricula_maior, matricula_menor = None, None

  # estado anterior
  matricula = int(input('Matrícula: '))

  while matricula != -7: # condic. de continuidade
    # trabalho
    nota1 = get_decimal_in_range('Nota 1: ', 0.0, 10.0)
    nota2 = get_decimal_in_range('Nota 2: ', 0.0, 10.0)
    qtd_aluno += 1

    media = (nota1 + nota2) / 2

    situacao = calcular_situacao(media)

    if situacao == 'AP':
      qtd_aprovado += 1
    elif situacao == 'PF':
      qtd_provafinal += 1
    else:
      qtd_reprovado += 1

    # maior e manor média
    if media > maior_media:
      maior_media = media
      matricula_maior = matricula
    
    if media < menor_media:
      menor_media = media
      matricula_menor = matricula

    # convergencia:
    input('Enter to continue...')
    limpar_tela()
    matricula = int(input('Matrícula: '))

  # resultado
  resultado = f'''
  >>>> ACADEMICO <<<<
  Alunos: {qtd_aluno}
  \tAprovados  : {qtd_aprovado}
  \tProva Final: {qtd_provafinal}
  \tReprovados : {qtd_reprovado}
  Estatísticas:
  \tMaior Média: {maior_media:.2f} (Aluno: {matricula_maior})
  \tMenor Média: {menor_media: .2f} (Aluno: {matricula_menor})
  ''' if qtd_aluno > 0 else 'Não há alunos cadastrados!'
  
  print(resultado)
  print('Fim.')


def limpar_tela():
  os.system('clear')

# features
def calcular_situacao(media: float):
  if media < 4:
    return 'RP'
  elif media < 7:
    return 'PF'
  else:
    return 'AP'


# utils
def get_decimal_in_range(label: str, min_value: float, max_value: float):
  numero = get_decimal_number(label)

  while numero < min_value or numero > max_value:
    print(f'Valor fora da faixa ({min_value}-{max_value})')
    numero = get_decimal_number(label)
  
  return numero


def get_decimal_number(label: str):
  entrada = input(label)

  try:
    numero_a = float(entrada)
    return numero_a
  except ValueError:
    print('Valor decimal inválido!')
    numero_b = get_decimal_number(label)
    return numero_b


main()