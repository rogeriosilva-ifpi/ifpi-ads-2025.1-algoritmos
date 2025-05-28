def principal():
  definicao = 'AGUA'
  cabecalho(definicao)
  
  nome = input('Nome: ')
  ano_nasc = int(input('Ano Nasci.: '))
  
  idade = calcular_idade(ano_nasc)
  
  print(f'Olá {nome}! que bom ter vc aqui ;)')
  print(f'Olha só neste ano vc completa {idade} anos.')



def calcular_idade(ano_nascimento):
  idade = 2025 - ano_nascimento
  return idade


def cabecalho(nome_programa):
  print('---------------------------')
  print(f'----< Programa {nome_programa} <-----')

# print(definicao)

principal()

